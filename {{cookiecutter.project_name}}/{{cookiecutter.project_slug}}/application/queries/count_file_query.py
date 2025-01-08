from __future__ import annotations


class CountFileQuery:
    """Encapsulates input parameters for counting file operations."""

    def __init__(self, file_name: str, operations: list[str]):
        self.file_name = file_name
        self.operations = operations
