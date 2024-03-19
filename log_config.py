# log_config.py

import logging

def setup_logging():
    """
    Sets up the logging configuration for the Library Management System.
    It specifies the log file name, the log level, and the log message format.
    """
    logging.basicConfig(filename='library_system.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')
