# training_data/download_datasets.py
import os
import requests

class DatasetManager:
    def __init__(self, dataset_url, dataset_path="data/training_data/"):
        """
        Initializes the DatasetManager with a URL to download the dataset
        and a path where the dataset should be stored.
        """
        self.dataset_url = dataset_url
        self.dataset_path = dataset_path

    def download_dataset(self):
        """
        Downloads the dataset from the given URL and saves it to the specified path.
        """
        if not os.path.exists(self.dataset_path):
            os.makedirs(self.dataset_path)

        dataset_name = self.dataset_url.split("/")[-1]
        dataset_file_path = os.path.join(self.dataset_path, dataset_name)

        print(f"Downloading dataset from {self.dataset_url}...")
        response = requests.get(self.dataset_url)

        if response.status_code == 200:
            with open(dataset_file_path, 'wb') as f:
                f.write(response.content)
            print(f"Dataset saved to {dataset_file_path}")
        else:
            print(f"Failed to download dataset. Status code: {response.status_code}")

# Example usage:
if __name__ == "__main__":
    dataset_manager = DatasetManager(
        dataset_url="https://example.com/sample-dataset.csv"
    )
    dataset_manager.download_dataset()
