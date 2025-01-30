import unittest
from {{cookiecutter.project_slug}}.application.handlers.count_file_handler import CountFileHandler
from unittest.mock import Mock

class TestCountFileHandler(unittest.TestCase):
    def setUp(self):
        self.file_processor_service = Mock()
        self.handler = CountFileHandler(self.file_processor_service)

    def test_handle_with_words_operation(self):
        # Arrange
        query = Mock(file_name="test.txt", operations=["words"])
        expected_result = {"words": 10}
        self.file_processor_service.process.return_value = expected_result

        # Act
        result = self.handler.handle(query)

        # Assert
        self.assertEqual(result, expected_result)
        self.file_processor_service.process.assert_called_once_with("test.txt", ["words"])

    def test_handle_with_characters_operation(self):
        # Arrange
        query = Mock(file_name="test.txt", operations=["characters"])
        expected_result = {"characters": 50}
        self.file_processor_service.process.return_value = expected_result

        # Act
        result = self.handler.handle(query)

        # Assert
        self.assertEqual(result, expected_result)
        self.file_processor_service.process.assert_called_once_with("test.txt", ["characters"])

    def test_handle_with_both_operations(self):
        # Arrange
        query = Mock(file_name="test.txt", operations=["words", "characters"])
        expected_result = {"words": 10, "characters": 50}
        self.file_processor_service.process.return_value = expected_result

        # Act
        result = self.handler.handle(query)

        # Assert
        self.assertEqual(result, expected_result)
        self.file_processor_service.process.assert_called_once_with("test.txt", ["words", "characters"])

if __name__ == "__main__":
    unittest.main()
