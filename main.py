import os
import re
import html
from typing import Union, List, Optional

from google.cloud import translate_v2 as translate
from google.oauth2 import service_account

credentials = service_account.Credentials.from_service_account_file(
    'handy-station-415405-198eaa66d90a.json')

# scoped_credentials = credentials.with_scopes(
#     ['https://www.googleapis.com/auth/cloud-platform'])


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


def main() -> None:
    # Get current folder
    current_directory: str = os.getcwd()

    # Get list of .md files
    md_files: List[str] = [f for f in os.listdir(current_directory) if f.endswith('.md') and f != 'README.md']

    # Converting each MD to GIFT
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
                print('TRANSLATE:', translated_question)
                gift_question: str = convert_to_gift(translated_question)
            else:
                gift_question: str = convert_to_gift(question)
            if gift_question:
                gift_questions.append(gift_question)

        # Recording list of questions into file
        if gift_questions:
            with open(os.path.join(current_directory, gift_file), 'w', encoding='utf-8') as f:
                for gift_question in gift_questions:
                    print('RECORD:', gift_question)
                    f.write(gift_question)
                    f.write('\n\n')


if __name__ == '__main__':
    main()

