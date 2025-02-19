import unittest
from unittest import mock
from unittest.mock import MagicMock, Mock, patch
import unittest.mock

from fastapi.testclient import TestClient

from {{cookiecutter.project_slug}}.adapters.http import create_http_app
from {{cookiecutter.project_slug}}.application.handlers.count_file_handler import CountFileHandler
from {{cookiecutter.project_slug}}.application.queries.count_file_query import CountFileQuery
from {{cookiecutter.project_slug}}.domain.ports.file_processor_port import FileProcessorPort


class TestHttpAdapter(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures before each test method."""
        self.mock_processor = Mock(spec=FileProcessorPort)
        self.mock_handler = Mock(spec=CountFileHandler)
        self.app = create_http_app(self.mock_handler)
        self.client = TestClient(self.app)


    def test_status_endpoint(self):
        """Test that the status endpoint returns the expected response."""
        response = self.client.get("/status")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_process_file_with_single_operation(self):
        expected_result = {"words": 42}
        self.mock_handler.handle.return_value = expected_result

        response = self.client.get(
            "/process-file",
            params={ "file": "test.txt", "operations": ["words"] }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.mock_handler.handle.call_count, 1)
        self.assertEqual(response.json(), {"result": expected_result})
        self.mock_handler.handle.assert_called_once()
        query = CountFileQuery("test.txt", ["words"])
        self.assertEqual(self.mock_handler.handle.call_args[0][0].file_name, "test.txt")
        self.assertEqual(self.mock_handler.handle.call_args[0][0].operations, ["words"])


    def test_process_file_with_multiple_operations(self):
        expected_result = {"words": 42, "characters": 256}
        self.mock_handler.handle.return_value = expected_result

        response = self.client.get(
            "/process-file",
            params={
                "file": "test.txt",
                "operations": "words,characters"
            }
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": expected_result})
        self.assertEqual(self.mock_handler.handle.call_count, 1)
        self.mock_handler.handle.assert_called_once()
        self.assertEqual(self.mock_handler.handle.call_args[0][0].file_name, "test.txt")
        self.assertEqual(self.mock_handler.handle.call_args[0][0].operations, ["words", "characters"])

    def test_process_file_with_empty_operations(self):
        response = self.client.get(
            "/process-file",
            params={
                "file": "test.txt",
                "operations": []
            }
        )

        self.assertEqual(response.status_code, 422)
        expected_result = {"detail": [{"input": {"file": "test.txt"}, "loc": ["query", "operations"], "msg": "Field required","type": "missing"}]}
        self.assertEqual(response.json(),  expected_result)
        self.mock_handler.handle.assert_not_called()

    def test_process_file_missing_file_parameter(self):
        response = self.client.get(
            "/process-file",
            params={
                "operations": ["words"]
            }
        )

        self.assertEqual(response.status_code, 422)
        self.mock_processor.process.assert_not_called()

    def test_process_file_missing_operations_parameter(self):
        response = self.client.get(
            "/process-file",
            params={
                "file": "test.txt"
            }
        )
        self.assertEqual(response.status_code, 422)
        self.mock_processor.process.assert_not_called()

    def test_process_file_verifies_query_creation(self):
        file_name = "test.txt"
        operations = ["words"]
        expected_result = {"words": 42}
        self.mock_handler.handle.return_value = expected_result

        response = self.client.get(
            "/process-file",
            params={
                "file": file_name,
                "operations": operations
            }
        )
        self.assertEqual(response.status_code, 200)
        
        actual_query = self.mock_handler.handle.call_args[0][0]
        expected_query = CountFileQuery(file_name, operations)
        self.assertEqual(actual_query.file_name, expected_query.file_name)
        self.assertEqual(actual_query.operations, expected_query.operations)
        
        self.assertEqual(response.json(), {"result": expected_result})

if __name__ == "__main__":
    unittest.main()
