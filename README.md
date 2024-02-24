# MDtoGIFTconverter

## Description
MDtoGIFTconverter is a Python application that converts Markdown files containing multiple-choice questions into the GIFT format commonly used in educational platforms and assessment tools. This tool automates the process of converting questions written in Markdown syntax into a format compatible with various e-learning systems.

## Features
- Converts Markdown files (.md) containing multiple-choice questions into GIFT format (.gift).
- Preserves the structure of questions, including question numbers and options.
- Handles special characters such as `<`, `>`, `{`, `}`, etc., by escaping them appropriately.
- Supports batch conversion of multiple Markdown files within a directory.
- Simple to use with command-line interface.

## Installation
1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/your_username/MDtoGIFTconverter.git
    ```
2. Navigate to the project directory:
    ```bash
    cd MDtoGIFTconverter
    ```

## Usage
1. Ensure you have Python installed on your system.
2. Place your Markdown files containing multiple-choice questions in the same directory as the `main.py` file.
3. Run the `main.py` script:
    ```bash
    python main.py
    ```
4. The converted GIFT files will be generated in the same directory.

## Example
Suppose you have a Markdown file named `questions.md` with the following content:
```markdown
#### Q1. What is the capital of France?
- [x] Paris
- [ ] Rome
- [ ] Berlin

#### Q2. Which planet is known as the Red Planet?
- [x] Mars
- [ ] Venus
- [ ] Jupiter

Running the MDtoGIFTconverter on this file will generate a GIFT file named `questions.gift` with the following content:
```plaintext
What is the capital of France?{ =Paris ~Rome ~Berlin }
Which planet is known as the Red Planet?{ =Mars ~Venus ~Jupiter }```
```

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License




