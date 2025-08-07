import logzero
from logzero import logger
import datetime
import os
import logging

class HTMLFormatter(logging.Formatter):
    def format(self, record):
        color_map = {
            'INFO': 'green',
            'WARNING': 'orange',
            'ERROR': 'red',
            'CRITICAL': 'darkred',
            'DEBUG': 'blue'
        }
        color = color_map.get(record.levelname, 'black')
        message = super().format(record)
        return f'<p style="color:{color};">{message}</p>'


def setup_logzero_logger():
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_dir_path = "C:/Users/10835846/PycharmProjects/ProjectGladiator/logs"
    os.makedirs(log_dir_path, exist_ok=True)
    filename = f"log_{timestamp}.html"
    log_file_path = os.path.join(log_dir_path, filename)

    logzero.logfile(log_file_path, maxBytes=1e6, backupCount=3)
    logzero.loglevel(logging.DEBUG)

    for handler in logger.handlers:
        if isinstance(handler, logging.FileHandler):
            formatter = HTMLFormatter("%(asctime)s - %(levelname)s - %(message)s")
            handler.setFormatter(formatter)

    return logger
