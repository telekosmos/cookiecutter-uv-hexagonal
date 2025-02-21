import logging

from {{cookiecutter.project_slug}}.adapters.http import create_http_app
from {{cookiecutter.project_slug}}.adapters.default_logger import DefaultLoggerAdapter
from {{cookiecutter.project_slug}}.adapters.repositories.file_reader import FileReaderAdapter
from {{cookiecutter.project_slug}}.application.handlers.count_file_handler import CountFileHandler
from {{cookiecutter.project_slug}}.domain.ports.logger_port import LoggerPort
from {{cookiecutter.project_slug}}.domain.services.file_processor_service import FileProcessorService

# Instantiate the FileReaderAdapter (driven adapter)
file_reader_adapter = FileReaderAdapter()

# Instantiate the LoggerAdapter (driven adapter)
logger: LoggerPort = DefaultLoggerAdapter(log_level=logging.DEBUG)

# Instantiate the FileProcessorService (business logic)
file_processor_service = FileProcessorService(logger, file_reader_adapter)

# Instantiate the Query Handler
count_file_handler = CountFileHandler(file_processor_service)

# Run HTTP interface
app = create_http_app(logger, count_file_handler)

def start():
    import uvicorn
    uvicorn.run("{{cookiecutter.project_slug}}.main_http:app", host="0.0.0.0", port=8000, reload=True)

if __name__ == "__main__":
    start()
