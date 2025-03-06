from abc import ABC, abstractmethod
from typing import Any, Optional


class ConfigPort(ABC):
    @abstractmethod
    def get(self, key: str, default: Optional[Any]) -> Any: ...
