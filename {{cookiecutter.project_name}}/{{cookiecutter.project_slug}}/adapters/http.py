from typing import Annotated

from pydantic import BaseModel
from fastapi import FastAPI, Query
from {{cookiecutter.project_slug}}.application.handlers.count_file_handler import CountFileHandler
from {{cookiecutter.project_slug}}.application.queries.count_file_query import CountFileQuery


class FileProcessingRequest(BaseModel):
    file: str
    operations: str

class HttpApp:
    def __init__(self, query_handler: CountFileHandler):
        self.app = FastAPI()
        self.query_handler = query_handler

        @self.app.get("/status")
        async def status():
            return {"status": "ok"}

        @self.app.get("/process-file")
        async def process_file(request: Annotated[FileProcessingRequest, Query()]):
            query = CountFileQuery(file_name=request.file, operations=request.operations.split(","))
            print(query)
            result = query_handler.handle(query)
            return {"result": result}

def create_http_app(query_handler: CountFileHandler):
    """Creates an HTTP app for processing files."""
    http_app = HttpApp(query_handler)
    return http_app.app
