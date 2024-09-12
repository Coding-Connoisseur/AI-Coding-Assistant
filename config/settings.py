# settings.py

import os

class Settings:
    """
    Holds project-wide settings and default configurations.
    Provides methods to update and retrieve settings dynamically.
    """

    def __init__(self):
        # Default settings
        self.api_base_url = "http://localhost:5000/"
        self.default_language = "python"
        self.default_log_level = "INFO"
        
        # Directory paths
        self.log_dir = "data/logs/"
        self.dataset_dir = "data/training_data/"
        
        # OpenAI API key (can be loaded from environment variables)
        self.openai_api_key = os.getenv("OPENAI_API_KEY", "your_openai_api_key")

        # Additional configurations (can be environment-specific)
        self.environment = os.getenv("ENV", "development")
        self.debug_mode = self.environment == "development"
        
    def update_setting(self, key, value):
        """
        Updates the specified setting with a new value.
        """
        setattr(self, key, value)

    def get_setting(self, key):
        """
        Retrieves the value of a specific setting. Returns None if the setting doesn't exist.
        """
        return getattr(self, key, None)

    def load_from_env(self):
        """
        Loads relevant settings from environment variables.
        """
        self.api_base_url = os.getenv("API_BASE_URL", self.api_base_url)
        self.default_language = os.getenv("DEFAULT_LANGUAGE", self.default_language)
        self.default_log_level = os.getenv("LOG_LEVEL", self.default_log_level)
        self.log_dir = os.getenv("LOG_DIR", self.log_dir)
        self.dataset_dir = os.getenv("DATASET_DIR", self.dataset_dir)
        self.openai_api_key = os.getenv("OPENAI_API_KEY", self.openai_api_key)
        self.environment = os.getenv("ENV", self.environment)
        self.debug_mode = self.environment == "development"

    def print_current_settings(self):
        """
        Prints the current configuration settings for debugging purposes.
        """
        print(f"API Base URL: {self.api_base_url}")
        print(f"Default Language: {self.default_language}")
        print(f"Log Directory: {self.log_dir}")
        print(f"Dataset Directory: {self.dataset_dir}")
        print(f"OpenAI API Key: {self.openai_api_key}")
        print(f"Environment: {self.environment}")
        print(f"Debug Mode: {self.debug_mode}")

# Example usage
if __name__ == "__main__":
    settings = Settings()
    
    # Load from environment variables if needed
    settings.load_from_env()
    
    # Print current settings
    settings.print_current_settings()

    # Update settings dynamically
    settings.update_setting("default_language", "javascript")
    print(f"Updated Language: {settings.get_setting('default_language')}")
