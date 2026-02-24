import logging
import logging.handlers
from pathlib import Path
import sys


class LoggingConfig:
    """Centralized logging configuration for the application."""

    def __init__(self, log_level: str = "INFO", log_dir: str = "logs"):
        """
        Initialize logging configuration.

        Args:
            log_level: The minimum logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
            log_dir: Directory to store log files
        """
        self.log_level = getattr(logging, log_level.upper())
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)

        # Define log file paths
        self.info_log_file = self.log_dir / "info.log"
        self.error_log_file = self.log_dir / "error.log"

        # Setup logging
        self._setup_logging()

    def _setup_logging(self):
        """Configure all logging handlers and formatters."""
        # Create formatters
        console_formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        file_formatter = logging.Formatter(
            fmt="%(asctime)s - %(name)s - %(levelname)s - %(filename)s:%(lineno)d - %(funcName)s() - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        # Configure root logger
        root_logger = logging.getLogger()
        root_logger.setLevel(self.log_level)

        # Clear existing handlers
        root_logger.handlers.clear()

        # Console handler - INFO and above
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(console_formatter)

        # File handler for INFO and above (with rotation)
        info_file_handler = logging.handlers.RotatingFileHandler(
            filename=self.info_log_file,
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,
            encoding="utf-8",
        )
        info_file_handler.setLevel(logging.INFO)
        info_file_handler.setFormatter(file_formatter)

        # File handler for ERROR and above (with rotation)
        error_file_handler = logging.handlers.RotatingFileHandler(
            filename=self.error_log_file,
            maxBytes=10 * 1024 * 1024,  # 10MB
            backupCount=5,
            encoding="utf-8",
        )
        error_file_handler.setLevel(logging.ERROR)
        error_file_handler.setFormatter(file_formatter)

        # Add handlers to root logger
        root_logger.addHandler(console_handler)
        root_logger.addHandler(info_file_handler)
        root_logger.addHandler(error_file_handler)

    def get_logger(self, name: str) -> logging.Logger:
        """
        Get a logger with the specified name.

        Args:
            name: Logger name (usually __name__)

        Returns:
            Configured logger instance
        """
        return logging.getLogger(name)


# Global logging configuration instance
logging_config = LoggingConfig()


def get_logger(name: str) -> logging.Logger:
    """
    Convenience function to get a logger.

    Args:
        name: Logger name (usually __name__)

    Returns:
        Configured logger instance
    """
    return logging_config.get_logger(name)
