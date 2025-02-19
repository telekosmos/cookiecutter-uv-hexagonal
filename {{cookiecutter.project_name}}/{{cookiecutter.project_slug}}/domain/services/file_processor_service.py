from {{cookiecutter.project_slug}}.domain.ports.file_processor_port import FileProcessorPort
from {{cookiecutter.project_slug}}.domain.ports.file_reader_port import FileReaderPort


class FileProcessorService(FileProcessorPort):
    """Service to process files and count words or characters."""
    
    def __init__(self, file_reader: 'FileReaderPort'):
        self.file_reader = file_reader  # Dependency injection of the file reader
    
    def process(self, file_name: str, operations: list[str]) -> dict:
        """Processes the file and counts words and/or characters."""
        content = self.file_reader.read(file_name)
        result = {}
        print(f"operations: {operations}")
        if "words" in operations:
            result["words"] = self.count_words(content)
        if "characters" in operations:
            result["characters"] = self.count_characters(content)
        if ["words", "characters"] == operations:
            result = {"characters": self.count_characters(content), "words": self.count_words(content)}

        return result
    
    def count_words(self, content: str) -> int:
        """Counts the number of words in the content."""
        return len(content.split())
    
    def count_characters(self, content: str) -> int:
        """Counts the number of characters in the content."""
        return len(content)
