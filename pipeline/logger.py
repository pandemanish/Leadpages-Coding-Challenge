import logging
import os


class Logger:
    def __init__(self, logs_dir='logs'):
        # logs folder check
        os.makedirs(logs_dir, exist_ok=True)
        
        # setup loggers for each type
        self.info_logger = self._setup_logger('info', os.path.join(logs_dir, 'info.log'), level=logging.INFO)
        self.error_logger = self._setup_logger('error', os.path.join(logs_dir, 'info.log'), level=logging.ERROR)
        self.notify_logger = self._setup_logger('notify', os.path.join(logs_dir, 'info.log'), level=logging.INFO)

    def _setup_logger(self, name, log_file, level=logging.INFO):
        # logger config
        logger = logging.getLogger(name)
        if not logger.handlers:
            logger.setLevel(level)
            handler = logging.FileHandler(log_file)
            handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
            logger.addHandler(handler)
        return logger
    
    def info(self, message):
        self.info_logger.info(message)

    def error(self, message):
        self.error_logger.error(message)

    def notify(self, message):
        self.notify_logger.info(message)