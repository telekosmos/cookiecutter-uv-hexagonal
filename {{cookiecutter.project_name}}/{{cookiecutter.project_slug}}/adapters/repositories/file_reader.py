from {{cookiecutter.project_slug}}.domain.ports.file_reader_port import FileReaderPort

class FileReaderAdapter(FileReaderPort):
    """Implementation of the file reader port."""
    
    def read(self, file_name: str) -> str:
        """Reads the content of a file and returns it."""
        try:
            with open(file_name, "r") as file:
                return file.read()
        except FileNotFoundError:
            raise Exception(f"File '{file_name}' not found.")
