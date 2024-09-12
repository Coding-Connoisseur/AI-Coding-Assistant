# environment.py
import os

class EnvironmentConfig:
    """
    Manages environment-specific configurations.
    """
    def __init__(self):
        self.environment = os.getenv('ENV', 'development')  # Default to development
        self.settings = self.load_environment_settings()

    def load_environment_settings(self):
        """
        Loads environment-specific settings based on the current environment.
        """
        if self.environment == 'development':
            return {
                "debug": True,
                "api_base_url": "http://localhost:5000/",
                "log_level": "DEBUG",
            }
        elif self.environment == 'production':
            return {
                "debug": False,
                "api_base_url": "https://api.production.com/",
                "log_level": "INFO",
            }
        else:
            raise ValueError(f"Unknown environment: {self.environment}")

    def get(self, key):
        """
        Retrieves the value for a specific setting in the current environment.
        """
        return self.settings.get(key)

# Example usage:
if __name__ == "__main__":
    env_config = EnvironmentConfig()
    print(f"Current environment: {env_config.environment}")
    print(f"API Base URL: {env_config.get('api_base_url')}")
    print(f"Debug mode: {env_config.get('debug')}")
