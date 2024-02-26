import tkinter as tk
from tkinter import filedialog
from ttkbootstrap import Style

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

def main():
    # Create the main application window
    root = tk.Tk()
    root.title("File List Generator")
    
    # Apply the ttkbootstrap style
    style = Style(theme='litera')
    
    # Create a frame for the button
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)  # Apply padding here
    
    # Create a generate button
    generate_btn = tk.Button(frame, text="Select Files and Generate file_list.txt", command=generate_file_list)
    generate_btn.pack(fill='x', expand=True, padx=10, pady=10)  # Optionally, add padding here for the button
    
    # Start the application
    root.mainloop()

if __name__ == "__main__":
    main()
