# logs/log_manager.py
import os
import logging

class LogManager:
    def __init__(self, log_dir="data/logs/", log_file="ai_assistant.log"):
        """
        Initializes the LogManager to manage logs for AI model operations, debugging, and performance.
        """
        self.log_dir = log_dir
        self.log_file = log_file

        if not os.path.exists(self.log_dir):
            os.makedirs(self.log_dir)

        self.log_path = os.path.join(self.log_dir, self.log_file)

        logging.basicConfig(filename=self.log_path, level=logging.INFO, 
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def log_message(self, level, message):
        """
        Logs a message to the log file with the specified level.
        """
        if level == 'info':
            logging.info(message)
        elif level == 'error':
            logging.error(message)
        elif level == 'warning':
            logging.warning(message)
        else:
            logging.debug(message)

    def get_log_file(self):
        """
        Returns the path of the log file.
        """
        return self.log_path

# Example usage:
if __name__ == "__main__":
    log_manager = LogManager()
    log_manager.log_message('info', 'AI assistant model started.')
    log_manager.log_message('error', 'Model encountered an error during training.')
    print(f"Logs are stored at {log_manager.get_log_file()}")
