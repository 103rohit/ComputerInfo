import logging
import os
from datetime import datetime


def setup_logger():
    """
    Sets up the logger with a log file named according to the current date.
    Log files are stored in a 'logs' directory, under a subdirectory named
    according to the current date.

    The logger is configured with a specific format to include the timestamp,
    line number, logger name, log level, and message. The log level is set to INFO.

    After setting up the logger, an initial log message is recorded to confirm
    that logging has started.

    :return: None
    """
    # Create the log file name using the current date
    LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y')}.log"

    # Create the directory name using the current date
    LOG_DIR = f"test_{datetime.now().strftime('%m_%d_%Y')}"

    # Create the full path for the logs directory
    logs_path = os.path.join(os.getcwd(), "logs", LOG_DIR)

    # Ensure the directory exists, creating it if necessary
    os.makedirs(logs_path, exist_ok=True)

    # Complete path to the log file
    LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

    # Configure the logger
    logging.basicConfig(
        filename=LOG_FILE_PATH,
        format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
        level=logging.INFO
    )

    # Log an initial message to indicate that logging has started
    logging.info("Logging has started")
