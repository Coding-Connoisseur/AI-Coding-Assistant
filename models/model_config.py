# model_config.py

class ModelConfig:
    def __init__(self):
        """
        Initializes the model configuration with default hyperparameters.
        """
        self.learning_rate = 2e-5
        self.batch_size = 16
        self.num_train_epochs = 3
        self.weight_decay = 0.01

    def update_hyperparameters(self, learning_rate=None, batch_size=None, num_train_epochs=None, weight_decay=None):
        """
        Updates the hyperparameters with the specified values.
        """
        if learning_rate is not None:
            self.learning_rate = learning_rate
        if batch_size is not None:
            self.batch_size = batch_size
        if num_train_epochs is not None:
            self.num_train_epochs = num_train_epochs
        if weight_decay is not None:
            self.weight_decay = weight_decay

    def get_config(self):
        """
        Returns the current configuration settings as a dictionary.
        """
        return {
            "learning_rate": self.learning_rate,
            "batch_size": self.batch_size,
            "num_train_epochs": self.num_train_epochs,
            "weight_decay": self.weight_decay
        }
