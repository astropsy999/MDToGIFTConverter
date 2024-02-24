import os
import re
import html


def extract_questions(markdown_text):
    questions = []
    current_question = None

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


def convert_to_gift(question_text):
    # Find the question and options in Markdown format
    question_match = re.match(r'^#### (Q\d+)\. (.+?)\n((?:- \[.\] .+\n)+)', question_text, re.MULTILINE)

    if not question_match:
        return None

    question_number = question_match.group(1)
    question = question_match.group(2).strip()
    options = re.findall(r'- \[(.)\] (.+?)\n', question_text)

    # Convert the question and options to GIFT format
    gift_question = f"{question}" + "{"
    gift_options = ''.join([f"{'=' if is_correct == 'x' else '~'}{html.escape(option)} " for is_correct, option in options])

    return f"{gift_question}{gift_options.strip().replace('{', '&#123;').replace('}', '&#125;')}" + "}"


def main():
    # Get current dir
    current_directory = os.getcwd()

    # Get List of .md files
    md_files = [f for f in os.listdir(current_directory) if f.endswith('.md')]

    # Convert every MD into GIFT
    for md_file in md_files:
        with open(os.path.join(current_directory, md_file), 'r', encoding='utf-8') as f:
            markdown_text = f.read()

        # Get question from MD
        questions = extract_questions(markdown_text)

        # create GIFT filename
        gift_file = os.path.splitext(md_file)[0] + '.gift'

        # Insert questions GIFT
        with open(os.path.join(current_directory, gift_file), 'w', encoding='utf-8') as f:
            for question in questions:
                gift_question = convert_to_gift(question)  # Convert each question to GIFT format
                if gift_question:
                    f.write(gift_question)
                    f.write('\n\n')  # Insert a blank line after each question


if __name__ == '__main__':
    main()
