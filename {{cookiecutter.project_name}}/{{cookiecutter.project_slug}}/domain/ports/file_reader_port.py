from abc import ABC, abstractmethod

class FileReaderPort(ABC):
    """Port to define file-reading functionality."""
    
    @abstractmethod
    def read(self, file_name: str) -> str:
        """Reads the content of a file and returns it as a string."""
        pass
