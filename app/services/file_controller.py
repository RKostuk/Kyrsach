import os


class FileController:
    def __init__(self, main_directory):
        self.main_directory = main_directory

    def read_file(self, dir_name, file_name):
        file_path = os.path.join(self.main_directory, dir_name, file_name)

        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            return f"File not found: {file_path}"
        except Exception as e:
            return f"Error reading file: {str(e)}"
