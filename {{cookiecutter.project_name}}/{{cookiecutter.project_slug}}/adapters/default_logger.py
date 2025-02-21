import logging

from {{cookiecutter.project_slug}}.domain.ports.logger_port import LoggerPort


class DefaultLoggerAdapter(LoggerPort):
    def __init__(self, logger_name='{{cookiecutter.project_slug}}', log_level=logging.INFO):
        """
        Initialize the logger with a specific name and log level.

        :param logger_name: Name of the logger (default: '{{cookiecutter.project_slug}}.')
        :param log_level: Logging level (default: logging.INFO)
        """
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)

        # Create a console handler if no handlers exist
        if not self.logger.handlers:
            console_handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            console_handler.setFormatter(formatter)
            self.logger.addHandler(console_handler)

    def debug(self, message: str) -> None:
        """
        Log a debug message.

        :param message: Debug message to log
        """
        self.logger.debug(message)

    def info(self, message: str) -> None:
        """
        Log an info message.

        :param message: Info message to log
        """
        self.logger.info(message)

    def warn(self, message: str) -> None:
        """
        Log a warning message.

        :param message: Warning message to log
        """
        self.logger.warning(message)

    def error(self, message: str, error: Exception) -> None:
        """
        Log an error message with an exception.

        :param message: Error message to log
        :param error: Exception associated with the error
        """
        self.logger.error(f"{message}: {str(error)}", exc_info=True)
