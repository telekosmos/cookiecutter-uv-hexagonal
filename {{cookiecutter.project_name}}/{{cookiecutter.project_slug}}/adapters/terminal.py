from __future__ import annotations

from application.handlers.count_file_handler import CountFileHandler
from application.queries.count_file_query import CountFileQuery


class TerminalAdapter:
    """Adapter for handling terminal input/output."""

    def __init__(self, query_handler: CountFileHandler):
        self.query_handler = query_handler

    def run(self):
        """Runs the CLI interface."""
        file_name = input("Enter the file name: ")
        operations = input("Enter the operations (words, characters, or both): ").split(",")

        query = CountFileQuery(file_name=file_name, operations=operations)
        result = self.query_handler.handle(query)

        print("Result:", result)
