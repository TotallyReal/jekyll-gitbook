import os
import logging


def create_logger(file_name: str) -> logging.Logger:
    # Get the directory and name of the Python script
    script_dir = os.path.dirname(os.path.abspath(file_name))
    script_name = os.path.splitext(os.path.basename(file_name))[0]

    # Create a 'log' directory if it doesn't exist
    log_dir = os.path.join(script_dir, '_log')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger(script_name)
    logger.setLevel(logging.INFO)

    # Configure logging
    log_file = os.path.join(log_dir, f'{script_name}.log')
    logger.addHandler(logging.FileHandler(log_file, encoding='utf-8'))

    # logging.basicConfig(filename=log_file, filemode='w', level=logging.INFO)

    # Receive the encoded text from Ruby
    return logger


def clear_file(logger: logging.Logger):
    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            handler.stream.truncate(0)
