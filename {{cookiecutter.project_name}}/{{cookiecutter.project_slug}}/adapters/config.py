from typing import Any, Optional

import config
import dotenv

from {{cookiecutter.project_slug}}.domain.ports.config_port import ConfigPort

dotenv.load_dotenv()

class Config(ConfigPort):
    def __init__(self, file_path: str | None = "config.json") -> None:
        self.file_path = file_path
        self.cfg = config.Config(file_path)

    def get(self, key: str, default: Optional[Any] = None) -> Any:
        try:
            return self.cfg[key]
        except config.ConfigError as ce:
            if default is not None:
                return default
            else:
                raise ce




