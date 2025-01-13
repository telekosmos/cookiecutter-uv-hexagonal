from {{cookiecutter.project_slug}}.adapters.repositories.file_reader import FileReaderAdapter
from {{cookiecutter.project_slug}}.domain.services.file_processor_service import FileProcessorService
from {{cookiecutter.project_slug}}.application.handlers.count_file_handler import CountFileHandler
from {{cookiecutter.project_slug}}.adapters.terminal import TerminalAdapter
# from adapters.http import create_http_app

if __name__ == "__main__":
    # Instantiate the FileReaderAdapter
    file_reader_adapter = FileReaderAdapter()
    
    # Instantiate the FileProcessorService
    file_processor_service = FileProcessorService(file_reader_adapter)
    
    # Instantiate the Query Handler
    count_file_handler = CountFileHandler(file_processor_service)
    
    # Option 1: Run terminal interface
    terminal_adapter = TerminalAdapter(count_file_handler)
    terminal_adapter.run()
    
    # Option 2: Run HTTP interface
    # app = create_http_app(count_file_handler)
    # app.run(port=5000)
