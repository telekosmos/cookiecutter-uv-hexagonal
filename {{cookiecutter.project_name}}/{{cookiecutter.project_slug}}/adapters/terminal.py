from __future__ import annotations

from {{cookiecutter.project_slug}}.application.handlers.count_file_handler import CountFileHandler
from {{cookiecutter.project_slug}}.application.queries.count_file_query import CountFileQuery
from {{cookiecutter.project_slug}}.domain.ports.logger_port import LoggerPort

class TerminalAdapter:
    """Adapter for handling terminal input/output."""

    def __init__(self, logger: LoggerPort, config: ConfigPort, query_handler: CountFileHandler):
        self.query_handler = query_handler
        self.logger = logger
        self.config = config

    def run(self):
        """Runs the CLI interface."""
        file_name = input("Enter the file name: ")
        operations = input("Enter the operations (words, characters, or both): ").split(",")

        config_allowed = self.config.get("application.operations", [])
        if not all(op in config_allowed for op in operations):
            self.logger.error(f"Invalid operation(s): {', '.join(operations)}")
            raise ValueError(f"Invalid operation(s): {', '.join(operations)}")
        
        query = CountFileQuery(file_name=file_name, operations=operations)
        result = self.query_handler.handle(query)

        self.logger.info(f"Result: {result}")
