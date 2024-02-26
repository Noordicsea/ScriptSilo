import os

def read_file_list(file_list_path):
    """Read file list and paths from the given file."""
    file_dict = {}
    with open(file_list_path, 'r') as file:
        for line in file:
            if ': ' in line:
                file_name, file_path = line.strip().split(': ')
                if os.path.isdir(file_path):
                    file_path = os.path.join(file_path, file_name)
                file_dict[file_name] = file_path
    return file_dict

def get_files_content(file_dict):
    """Return the contents of the files formatted as a single string."""
    content_list = []
    for file_name, file_path in file_dict.items():
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                content_list.append(f"{file_name}:\n{content}\n[END OF {file_name.upper()}]\n")
        except FileNotFoundError:
            content_list.append(f"Error: '{file_name}' not found at '{file_path}'.")
    return "".join(content_list)

if __name__ == "__main__":
    file_list_path = 'file_list.txt'
    file_dict = read_file_list(file_list_path)
    codebase = get_files_content(file_dict)
