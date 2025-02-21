from typing import Annotated

from fastapi import FastAPI, Query
from pydantic import BaseModel

from {{cookiecutter.project_slug}}.application.handlers.count_file_handler import CountFileHandler
from {{cookiecutter.project_slug}}.application.queries.count_file_query import CountFileQuery
from {{cookiecutter.project_slug}}.domain.ports.logger_port import LoggerPort


class FileProcessingRequest(BaseModel):
    file: str
    operations: str

class HttpApp:
    def __init__(self, logger: LoggerPort, query_handler: CountFileHandler):
        self.app = FastAPI()
        self.query_handler = query_handler
        self.logger = logger

        @self.app.get("/status")
        async def status():
            return {"status": "ok"}

        @self.app.get("/process-file")
        async def process_file(request: Annotated[FileProcessingRequest, Query()]):
            query = CountFileQuery(file_name=request.file, operations=request.operations.split(","))
            self.logger.info(f"query: CountFileQuery({query.file_name}, {query.operations})")
            result = query_handler.handle(query)
            return {"result": result}

def create_http_app(logger: LoggerPort, query_handler: CountFileHandler):
    """Creates an HTTP app for processing files."""
    http_app = HttpApp(logger=logger, query_handler=query_handler)
    return http_app.app
