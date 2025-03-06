import logging

from {{cookiecutter.project_slug}}.adapters.default_logger import DefaultLoggerAdapter
from {{cookiecutter.project_slug}}.adapters.config import Config
from {{cookiecutter.project_slug}}.adapters.repositories.file_reader import FileReaderAdapter
from {{cookiecutter.project_slug}}.adapters.terminal import TerminalAdapter
from {{cookiecutter.project_slug}}.application.handlers.count_file_handler import CountFileHandler
from {{cookiecutter.project_slug}}.domain.ports.logger_port import LoggerPort
from {{cookiecutter.project_slug}}.domain.ports.config_port import ConfigPort
from {{cookiecutter.project_slug}}.domain.services.file_processor_service import FileProcessorService


def main():
    logger: LoggerPort = DefaultLoggerAdapter(log_level=logging.DEBUG) 
    config: ConfigPort = Config()
    # Instantiate the FileReaderAdapter (driven adapter)
    file_reader_adapter = FileReaderAdapter()

    # Instantiate the FileProcessorService (business logic)
    file_processor_service = FileProcessorService(logger, file_reader_adapter)

    # Instantiate the Query Handler
    count_file_handler = CountFileHandler(file_processor_service)

    terminal_adapter = TerminalAdapter(logger, config, count_file_handler)
    terminal_adapter.run()

if __name__ == "__main__":
    main()
