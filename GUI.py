import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap import Style
from tkinter import filedialog
from ttkbootstrap.constants import *
from code_collection import read_file_list, get_files_content
from openai_model import process_question
import markdown
import webbrowser
import tempfile
import os
import html
import speech_recognition as sr  # Speech recognition import
from pynput import keyboard  # Pynput keyboard import
import threading  # Import threading for running speech recognition in a separate thread

# Initialize a Recognizer object
r = sr.Recognizer()

def transcribe_speech():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)
            text = r.recognize_google(audio)
            # Use tkinter's thread-safe method to insert text into the text entry
            text_entry.insert(tk.END, text)
    except Exception as e:
        print(f"Sorry, I did not get that. Error: {e}")


def start_transcribe_speech():
    # Start transcribe_speech in a separate thread to avoid freezing the GUI
    threading.Thread(target=transcribe_speech, daemon=True).start()


def on_press(key):
    if key == keyboard.Key.f8:  # Can change key to any of your choice
        transcribe_speech()

listener = keyboard.Listener(on_press=on_press)
listener.start()

def copy_to_clipboard():
    text = text_display.get("1.0", tk.END)
    root.clipboard_clear()
    root.clipboard_append(text)
    root.update()

def copy_codebase_to_clipboard():
    file_list_path = 'file_list.txt'
    file_dict = read_file_list(file_list_path)
    codebase = get_files_content(file_dict)
    root.clipboard_clear()
    root.clipboard_append(codebase)
    root.update()

def handle_prompt():
    file_list_path = 'file_list.txt'
    file_dict = read_file_list(file_list_path)
    codebase = get_files_content(file_dict)
    request = text_entry.get()
    response = process_question(codebase, request)
    text_display.delete("1.0", tk.END)
    text_display.insert(tk.END, response)

def generate_file_list():
    file_paths = filedialog.askopenfilenames()
    output_file = 'file_list.txt'
    content_lines = []
    for file_path in file_paths:
        file_name = file_path.split('/')[-1]
        line = f"{file_name}: {file_path}"
        content_lines.append(line)
    with open(output_file, 'w') as file:
        file.write('\n'.join(content_lines))
    print("File list has been generated.")

def update_codebase():
    generate_file_list()

def open_in_browser(md_text):
    escaped_md_text = escape_html(md_text)
    corrected_md_text = escaped_md_text.replace("```python", "```python\n")
    html_content = markdown.markdown(corrected_md_text)
    template_path = 'template.html'
    css_path = 'styles.css'

    with open(template_path, 'r') as file:
        template_html = file.read()

    full_html = template_html.replace('<!-- Markdown content will be injected here -->', html_content)

    with tempfile.NamedTemporaryFile('w', delete=False, suffix='.html') as f:
        f.write(full_html)
        temp_dir = os.path.dirname(f.name)
        temp_css_path = os.path.join(temp_dir, 'styles.css')
        with open(css_path, 'r') as css_file:
            with open(temp_css_path, 'w') as temp_css_file:
                temp_css_file.write(css_file.read())
    webbrowser.open_new_tab(f.name)

def open_in_browser_from_text_display():
    md_text = text_display.get("1.0", tk.END)
    open_in_browser(md_text)

def escape_html(text):
    return html.escape(text)

root = ttk.Window(themename='litera')
root.title("Ask the Codebase")
root.geometry("600x400")
root.minsize(300, 200)

# Create and configure styles for buttons
style = Style()
style.configure('Markdown.TButton', background='#ff9b71')  # For brown button
style.configure('G.TButton', background='#1b998b')  # For green button
style.configure('Y.TButton', background='#e84855')   # For gold button
style.configure('Prompt.TButton', foreground='black', background='#FFFD82')   # For gold button
style.configure('small.TLabel', font=("Helvetica", 8))

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

frame.columnconfigure(1, weight=1)
frame.rowconfigure(1, weight=1)

entry_label = ttk.Label(frame, text="Enter Prompt:")
entry_label.grid(row=0, column=0, sticky=tk.W)

text_entry = ttk.Entry(frame)
text_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 10))  # Added padding to the right of the entry
text_entry.bind("<Return>", lambda event: handle_prompt())

submit_button = ttk.Button(frame, text="Submit Prompt", command=handle_prompt, style='Prompt.TButton')
submit_button.grid(row=0, column=2, sticky=tk.W, padx=(10, 0), pady=5)  # Adjusted padding for separation and alignment

text_display = tk.Text(frame)
text_display.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)

markdown_button = ttk.Button(frame, 
                             text="Open in Markdown Viewer", 
                             command=open_in_browser_from_text_display,
                             style='Markdown.TButton')  # brown button
markdown_button.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(5,0))

update_button = ttk.Button(frame, 
                           text="Update Codebase", 
                           command=update_codebase,
                           style='Y.TButton')  # gold button
update_button.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(5,0))

copy_codebase_button = ttk.Button(frame, 
                                  text="Copy Codebase to Clipboard",
                                  command=copy_codebase_to_clipboard,
                                  style='G.TButton')  # green button
copy_codebase_button.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(5,0))

notification_label = ttk.Label(frame, text="Press F8 for Speech to Text. It will automatically cut off the recording if you pause for too long.", style="small.TLabel")
notification_label.grid(row=5, column=0, columnspan=3, pady=(5,0))

root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0, weight=1)

root.mainloop()
