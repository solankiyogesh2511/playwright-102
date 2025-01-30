import os
import logging
from datetime import datetime
from configparser import ConfigParser, NoSectionError, NoOptionError
import inspect

class LoggerHelper:
    
    @staticmethod
    def get_logger():
        config = ConfigParser(interpolation=None)
        config.read('pytest.ini')
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
            
        # Default values
        log_file = f"{log_dir}/default.log"
        log_cli = "False"
        log_level = "INFO"
        log_formatter = "%Y-%m-%d %H:%M:%S"
        
        try:
            log_file = config.get("Logs", "log_path", fallback=log_file)
            log_cli = config.get("Logs", "log_cli", fallback=log_cli)
            log_level = config.get("Logs", "log_cli_level", fallback=log_level).upper()
            log_formatter = config.get("Logs", "log_file_date_format", fallback=log_formatter)
        except (NoSectionError, NoOptionError):
            pass  # Use defaults if `pytest.ini` is missing or misconfigured
        
        log_level = getattr(logging, log_level, logging.INFO)
        
        # Get the logger name based on the calling function
        stack = inspect.stack()
        logger_name = stack[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
        
        if not logger.handlers:
            # File handler
            try:
                file_handler = logging.FileHandler(log_file, mode='a')
                file_handler.setLevel(log_level)
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt=log_formatter)
                file_handler.setFormatter(formatter)
                logger.addHandler(file_handler)
            except Exception as e:
                print(f"Error creating file handler: {e}")
            
            # Console handler
            if log_cli == "True":
                console_handler = logging.StreamHandler()
                console_handler.setLevel(log_level)
                formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt=log_formatter)
                console_handler.setFormatter(formatter)
                logger.addHandler(console_handler)
        
        return logger
    
    @staticmethod
    def log_info(message: str) -> None:
        LoggerHelper.get_logger().info(message)
        
    @staticmethod
    def log_error(message: str) -> None:
        LoggerHelper.get_logger().error(message)
        
    @staticmethod
    def log_debug(message: str) -> None:
        LoggerHelper.get_logger().debug(message)
        
    @staticmethod
    def log_warning(message: str) -> None:
        LoggerHelper.get_logger().warning(message)
        
    @staticmethod
    def log_exception(message: str) -> None:
        LoggerHelper.get_logger().exception(message)
        
    @staticmethod
    def log_critical(message: str) -> None:
        LoggerHelper.get_logger().critical(message)

# Usage
if __name__ == "__main__":
    LoggerHelper.log_info("This is an info message")
    LoggerHelper.log_error("This is an error message")
    LoggerHelper.log_debug("This is a debug message")
    LoggerHelper.log_warning("This is a warning message")
    try:
        raise ValueError("This is a test exception")
    except Exception as e:
        LoggerHelper.log_exception(f"Exception occurred: {e}")
    LoggerHelper.log_critical("This is a critical message")
