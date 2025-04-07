import unittest
from unittest.mock import Mock, patch
from {{cookiecutter.project_slug}}.adapters.terminal import TerminalAdapter
from {{cookiecutter.project_slug}}.application.queries.count_file_query import CountFileQuery
from {{cookiecutter.project_slug}}.application.handlers.count_file_handler import CountFileHandler
from {{cookiecutter.project_slug}}.domain.ports.config_port import ConfigPort
from {{cookiecutter.project_slug}}.domain.ports.logger_port import LoggerPort


class TestTerminalAdapter(unittest.TestCase):
    def setUp(self):
        self.mock_handler = Mock(CountFileHandler)
        self.mock_logger: LoggerPort = Mock(spec=LoggerPort)
        self.mock_config: ConfigPort = Mock(spec=ConfigPort)

    def test_terminal_adapter_run_with_words(self):
        # Mock the query handler to return a specific result
        self.mock_handler.handle.return_value = {"words": 10}
        self.mock_config.get.return_value = ["characters", "words"]
        # Create a TerminalAdapter instance
        adapter = TerminalAdapter(self.mock_logger, self.mock_config, self.mock_handler)

        # Simulate user inputs
        with patch('builtins.input', side_effect=['test.txt', 'words']):
            adapter.run()

            # Assert that the query handler was called with correct parameters
            assert self.mock_handler.handle.call_args[0][0].file_name == 'test.txt'
            assert self.mock_handler.handle.call_args[0][0].operations == ['words']

            # Assert that the result was printed
            # mock_print.assert_called_once_with("Result:", {"words": 10})
            self.mock_logger.info.assert_called_once_with("Result: {'words': 10}")


    def test_terminal_adapter_run_with_characters(self):
        # Mock the query handler to return a specific result
        self.mock_handler.handle.return_value = {"characters": 50}
        self.mock_config.get.return_value = ["characters", "words"]
        # Create a TerminalAdapter instance
        adapter = TerminalAdapter(self.mock_logger, self.mock_config, self.mock_handler)

        # Simulate user inputs
        with patch('builtins.input', side_effect=['example.txt', 'characters']):
            adapter.run()

            # Assert that the query handler was called with correct parameters
            assert self.mock_handler.handle.call_args[0][0].file_name == 'example.txt'
            assert self.mock_handler.handle.call_args[0][0].operations == ['characters']

            # Assert that the result was printed
            self.mock_logger.info.assert_called_once_with("Result: {'characters': 50}")


    def test_terminal_adapter_run_with_both_operations(self):
        # Mock the query handler to return a specific result
        self.mock_handler.handle.return_value = {"words": 10, "characters": 50}
        self.mock_config.get.return_value = ["characters", "words"]
        # Create a TerminalAdapter instance
        adapter = TerminalAdapter(self.mock_logger, self.mock_config, self.mock_handler)

        # Simulate user inputs
        with patch('builtins.input', side_effect=['test_file.txt', 'words,characters']):
            # with patch('builtins.print') as mock_print:
            adapter.run()

            # Assert that the query handler was called with correct parameters
            assert self.mock_handler.handle.call_args[0][0].file_name == 'test_file.txt'
            assert self.mock_handler.handle.call_args[0][0].operations == ['words', 'characters']

            # Assert that the result was printed
            self.mock_logger.info.assert_called_once_with("Result: {'words': 10, 'characters': 50}")

if __name__ == "__main__":
    unittest.main()
