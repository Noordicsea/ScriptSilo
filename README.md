# Script Silo
# Code Collection and GUI Interface

This project consists of a Python application that allows users to manage and interact with a collection of code files through a graphical user interface (GUI). It includes functionalities such as reading a list of file paths from a text file, displaying the content of these files in a unified format, speech-to-text input for search queries, and more. 

## Features

- Read and display code files from a specified list.
- Speech-to-text functionality to input prompts via microphone.
- Generate a file list for easy management of code files.
- Use OpenAI's GPT model to process questions about the codebase.
- View Markdown-formatted responses in a built-in browser.

## Installation

Before running this application, ensure you have Python installed on your system. This project was developed using Python 3.8, but it should be compatible with other versions that support the used packages.

### Required Python Packages

- `tkinter` for the GUI.
- `ttkbootstrap` for styled tkinter widgets.
- `speech_recognition` for converting speech to text.
- `pynput` for keyboard interactions.
- `markdown` for Markdown processing.
- `openai` for interacting with OpenAI's API.
- `webbrowser` and `tempfile` for opening Markdown content in a browser.

You can install the necessary Python packages using pip:

```bash
pip install ttkbootstrap speech_recognition pynput markdown openai
```

Note: `tkinter` is typically included with Python, but if it's not on your system, you may need to install it separately.

### OpenAI API Key

To use the OpenAI functionalities, you'll need an API key from OpenAI. Set your API key as an environment variable:

```bash
export OPENAI_API_KEY='your_api_key_here'
```

## Usage

To start the application, navigate to the directory containing the project files in your terminal, and run:

```bash
python main.py
```

### Generating a File List

1. Use the "Select Files and Generate file_list.txt" button to choose code files you want to include in your codebase.
2. The application will generate a `file_list.txt` file containing the paths to the selected files.

### Querying the Codebase

- Enter your query in the text box and press "Submit Prompt" or the Enter key to process your question using the codebase and OpenAI's model.
- Press F8 to start speech-to-text input.

## Contributing

Contributions are welcome! If you'd like to contribute, please fork the repository and use a feature branch. Pull requests are warmly welcomed.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
