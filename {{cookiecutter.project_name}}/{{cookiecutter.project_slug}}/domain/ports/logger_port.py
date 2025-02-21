from abc import ABC, abstractmethod


class LoggerPort(ABC):
    @abstractmethod
    def info(self, message: str) -> None:
        pass
    @abstractmethod
    def error(self, message: str, error: Exception) -> None:
        pass
    @abstractmethod
    def warn(self, message: str) -> None:
        pass
    @abstractmethod
    def debug(self, message: str) -> None:
        pass
