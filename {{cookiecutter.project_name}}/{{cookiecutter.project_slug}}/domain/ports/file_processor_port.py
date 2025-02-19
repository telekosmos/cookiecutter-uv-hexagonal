from abc import ABC, abstractmethod

class FileProcessorPort(ABC):
    @abstractmethod
    def process(self, filename: str, operations: list[str]) -> dict:
        pass
