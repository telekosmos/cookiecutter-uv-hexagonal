import unittest
from {{cookiecutter.project_slug}}.domain.services.file_processor_service import FileProcessorService
from {{cookiecutter.project_slug}}.domain.ports.logger_port import LoggerPort
from {{cookiecutter.project_slug}}.adapters.null_logger import NullLoggerAdapter


from unittest.mock import Mock

class TestFileProcessorService(unittest.TestCase):
    def setUp(self):
        self.logger = NullLoggerAdapter()
        self.file_reader = Mock()
        self.service = FileProcessorService(self.logger, self.file_reader)

    def test_process_with_words_operation(self):
        # Arrange
        file_name = "test.txt"
        operations = ["words"]
        content = "Hello world"
        self.file_reader.read.return_value = content

        # Act
        result = self.service.process(file_name, operations)

        # Assert
        self.assertEqual(result["words"], 2)
        self.file_reader.read.assert_called_once_with(file_name)

    def test_process_with_characters_operation(self):
        # Arrange
        file_name = "test.txt"
        operations = ["characters"]
        content = "Hello world"
        self.file_reader.read.return_value = content

        # Act
        result = self.service.process(file_name, operations)

        # Assert
        self.assertEqual(result["characters"], 11)
        self.file_reader.read.assert_called_once_with(file_name)

    def test_process_with_both_operations(self):
        # Arrange
        file_name = "test.txt"
        operations = ["words", "characters"]
        content = "Hello world"
        self.file_reader.read.return_value = content

        # Act
        result = self.service.process(file_name, operations)

        # Assert
        self.assertEqual(result["words"], 2)
        self.assertEqual(result["characters"], 11)
        self.file_reader.read.assert_called_once_with(file_name)

    def test_count_words(self):
        # Arrange
        content = "Hello world"

        # Act
        result = self.service.count_words(content)

        # Assert
        self.assertEqual(result, 2)

    def test_count_characters(self):
        # Arrange
        content = "Hello world"

        # Act
        result = self.service.count_characters(content)

        # Assert
        self.assertEqual(result, 11)

if __name__ == "__main__":
    unittest.main()
