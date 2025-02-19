from {{cookiecutter.project_slug}}.adapters.repositories.file_reader import FileReaderAdapter
from {{cookiecutter.project_slug}}.domain.services.file_processor_service import FileProcessorService
from {{cookiecutter.project_slug}}.application.handlers.count_file_handler import CountFileHandler
from {{cookiecutter.project_slug}}.adapters.terminal import TerminalAdapter

def main():
    # Instantiate the FileReaderAdapter (driven adapter)
    file_reader_adapter = FileReaderAdapter()

    # Instantiate the FileProcessorService (business logic)
    file_processor_service = FileProcessorService(file_reader_adapter)

    # Instantiate the Query Handler
    count_file_handler = CountFileHandler(file_processor_service)

    terminal_adapter = TerminalAdapter(count_file_handler)
    terminal_adapter.run()

if __name__ == "__main__":
    main()
