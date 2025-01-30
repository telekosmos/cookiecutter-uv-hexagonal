from __future__ import annotations

from {{cookiecutter.project_slug}}.domain.services.file_processor_service import FileProcessorService


class CountFileHandler:
    """Handles the file-counting query."""

    def __init__(self, file_processor_service: FileProcessorService):
        self.file_processor_service = file_processor_service

    def handle(self, query: 'CountFileQuery') -> dict:  # noqa: UP037
        """Handles the query and invokes the domain service."""
        return self.file_processor_service.process(query.file_name, query.operations)
