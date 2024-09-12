# training.py
from transformers import Trainer, TrainingArguments, GPT2Tokenizer, GPT2LMHeadModel
from datasets import load_dataset

class ModelTraining:
    def __init__(self, model_name="gpt2", dataset_name="codeparrot/code_instructions"):
        """
        Initializes the training class with a specific model and dataset.
        Default: GPT-2 model, CodeParrot dataset.
        """
        self.tokenizer = GPT2Tokenizer.from_pretrained(model_name)
        self.model = GPT2LMHeadModel.from_pretrained(model_name)
        self.dataset = load_dataset(dataset_name)

    def tokenize_function(self, examples):
        """
        Tokenizes the input examples for training.
        """
        return self.tokenizer(examples['text'], padding="max_length", truncation=True, max_length=128)

    def prepare_data(self):
        """
        Prepares the dataset for training by tokenizing the data.
        """
        tokenized_dataset = self.dataset.map(self.tokenize_function, batched=True)
        return tokenized_dataset

    def fine_tune_model(self):
        """
        Fine-tunes the pre-trained model on the tokenized dataset.
        """
        tokenized_dataset = self.prepare_data()
        
        training_args = TrainingArguments(
            output_dir="./results",
            evaluation_strategy="epoch",
            learning_rate=2e-5,
            per_device_train_batch_size=16,
            per_device_eval_batch_size=16,
            num_train_epochs=3,
            weight_decay=0.01
        )

        trainer = Trainer(
            model=self.model,
            args=training_args,
            train_dataset=tokenized_dataset['train'],
            eval_dataset=tokenized_dataset['validation']
        )

        trainer.train()

    def evaluate_model(self):
        """
        Evaluates the model performance on the validation set.
        """
        trainer = Trainer(model=self.model)
        eval_results = trainer.evaluate()
        return eval_results
