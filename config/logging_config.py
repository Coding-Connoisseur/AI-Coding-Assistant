# logging_config.py
import logging
import os

class LoggingConfig:
    """
    Configures logging settings for the AI assistant.
    """
    def __init__(self, log_dir="data/logs/", log_file="ai_assistant.log"):
        self.log_dir = log_dir
        self.log_file = log_file
        self.log_path = os.path.join(self.log_dir, self.log_file)

        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        # Configure logging settings
        logging.basicConfig(
            filename=self.log_path,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
        )

    def get_logger(self, name):
        """
        Returns a logger instance with the given name.
        """
        return logging.getLogger(name)

# Example usage:
if __name__ == "__main__":
    log_config = LoggingConfig()
    logger = log_config.get_logger(__name__)
    logger.info("AI assistant has started.")
    logger.error("An error occurred.")
