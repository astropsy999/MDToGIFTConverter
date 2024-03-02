import html
import os
import re
import sys
from typing import Union, List, Optional

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QMessageBox
from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    'handy-station-415405-198eaa66d90a.json')

TO_TRANSLATE = False
# TO_TRANSLATE = 'uk'

# API_KEY = os.getenv('API_KEY')


def translate_text(text: Union[str, bytes]) -> str:
    # Init Google Cloud Translate API
    translate_client = translate.Client(credentials=credentials)

    # Define language
    result = translate_client.detect_language(text)

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    source_language = result['language']

    if source_language != TO_TRANSLATE:
        result = translate_client.translate(text, target_language=TO_TRANSLATE)
        return result['translatedText']
    else:
        return text


def extract_questions(markdown_text: str) -> List[str]:
    questions: List[str] = []
    current_question: str = None

    for line in markdown_text.split('\n'):
        if line.startswith('#### Q'):
            if current_question:
                questions.append(current_question)
            current_question = line + '\n'
        elif line.startswith('- ['):
            current_question += line + '\n'

    if current_question:
        questions.append(current_question)

    return questions


def convert_to_gift(question_text: str) -> Optional[str]:
    # Find the question and options in Markdown format
    question_match = re.match(r'^#### (Q\d+)\. (.+?)\n((?:- \[.\] .+\n)+)', question_text, re.MULTILINE)

    if not question_match:
        return None

    question_number = question_match.group(1)
    question = question_match.group(2).strip()

    # Adjust the regular expression pattern to match all options at once
    options = re.findall(r'- \[(.)\] (.+?)\n', question_match.group(3))

    # Convert the question and options to GIFT format
    gift_question = f"{question}" + " {"
    gift_options = ''.join(
        [f"={'#' if is_correct == 'x' else ''}{html.escape(option)} " for is_correct, option in options])

    return f"{gift_question}{gift_options.strip().replace('{', '&#123;').replace('}', '&#125;')}" + "}"


def list_md_files() -> List[str]:
    """Get list of .md files in the current directory."""
    current_directory: str = os.getcwd()
    md_files: List[str] = [f for f in os.listdir(current_directory) if f.endswith('.md') and f != 'README.md']
    return md_files


def show_markdown_files_dialog(md_files: List[str]) -> None:
    message = "Markdown files found in the current directory:\n"
    for idx, md_file in enumerate(md_files, start=1):
        message += f"{idx}. {md_file}\n"

    message_box = QMessageBox()
    message_box.setText(message)
    message_box.setWindowTitle("Markdown Files")
    message_box.exec()


def convert_files_to_gift(md_files: List[str], current_directory: str) -> None:
    for md_file in md_files:
        with open(os.path.join(current_directory, md_file), 'r', encoding='utf-8') as f:
            markdown_text: str = f.read()

        # Get questions from MD
        questions: List[str] = extract_questions(markdown_text)

        # Creating GIFT filename
        if not TO_TRANSLATE:
            gift_file: str = os.path.splitext(md_file)[0] + '.gift'
        else:
            gift_file: str = os.path.splitext(md_file)[0] + '_' + TO_TRANSLATE + '.gift'

        # Inserting questions to GIFT
        gift_questions: List[str] = []
        for question in questions:
            if TO_TRANSLATE:
                translated_question: str = translate_text(question)
                translated_question = translated_question['translatedText']
                gift_question: str = convert_to_gift(translated_question)
            else:
                gift_question: str = convert_to_gift(question)
            if gift_question:
                gift_questions.append(gift_question)

        # Recording list of questions into file
        if gift_questions:
            with open(os.path.join(current_directory, gift_file), 'w', encoding='utf-8') as f:
                for gift_question in gift_questions:
                    f.write(gift_question)
                    f.write('\n\n')


def main() -> None:
    app = QApplication(sys.argv)

    current_directory: str = os.getcwd()
    md_files: List[str] = list_md_files()

    if not md_files:
        QMessageBox.information(None, "Information", "No Markdown files found in the current directory.")
        return

    show_markdown_files_dialog(md_files)

    reply = QMessageBox.question(None, "Confirmation", "Convert all files to GIFT format?", QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

    if reply == QMessageBox.StandardButton.Yes:
        convert_files_to_gift(md_files, current_directory)
        QMessageBox.information(None, "Information", "Conversion completed.")
    elif reply == QMessageBox.StandardButton.No:
        QMessageBox.information(None, "Information", "Conversion aborted.")
    else:
        QMessageBox.warning(None, "Warning", "Invalid input. Please enter 'yes' or 'no'.")

    sys.exit(app.exec())


if __name__ == '__main__':
    main()

