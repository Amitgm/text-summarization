# TEXT-SUMMARIZATION TOOL

The Text Summarization Tool is a powerful application that uses the google/pegasus-cnn_dailymail model to generate concise and accurate summaries of input texts. Built with Flask and Python, this tool leverages a fine-tuned Seq2Seq model to provide high-quality summaries for long articles, documents, or any text input.

The ML-Ops Pipeline for the Text Summarization Tool is a robust and scalable workflow that ensures the seamless development, deployment, and monitoring of the machine learning model. Below is a detailed breakdown of each stage in the pipeline

#### Data Ingestion

The first stage involves collecting and preparing the raw data required for training and fine-tuning the model.

#### Data Preprocessing

Raw data is cleaned, transformed, and prepared for training the model.

- Text Cleaning: Remove unnecessary characters, stopwords, and special symbols.

- Tokenization: Split the text into tokens (words or subwords) for model input.

- Dataset Splitting: Divide the data into training, validation, and test sets (e.g., 80% training, 10% validation, 10% testing).

####  Model Training

- Model Selection: Choose the google/pegasus-cnn_dailymail model, a pre-trained Seq2Seq model optimized for summarization tasks.

- Fine-Tuning: Fine-tune the model on the preprocessed dataset to adapt it to the specific summarization task.

- Hyperparameter Tuning: Experiment with hyperparameters (e.g., learning rate, batch size, epochs) to optimize model performance.

#### Model Evaluation

- The trained model is evaluated to ensure it meets the desired performance metrics.



## Features

- State-of-the-Art Model: Utilizes the google/pegasus-cnn_dailymail model, a pre-trained Seq2Seq model fine-tuned for summarization tasks.

- User-Friendly Interface: A clean and intuitive web interface with an input text box and a summary output box.

- Fast and Efficient: Summarizes text in real-time with minimal latency.

- Customizable: Easily extendable for additional features or integration with other tools.

## Model Details

- Model Name: google/pegasus-cnn_dailymail

- Architecture: Seq2Seq (Transformer-based)

- Fine-Tuning: Fine-tuned on the cnn_dailymail dataset for optimal summarization performance.

## How It Works

The tool uses the Pegasus model, which is a transformer-based Seq2Seq model pre-trained on large datasets and fine-tuned for summarization tasks. The model takes in a long text input and generates a concise       summary by identifying the most important information.

<div align="center">
    <img src="./Images/text-summarization.png" alt="Summarization Results" width="1200">
    <p><em>Text Summarizer.</em></p>
</div>


## Installation

Follow these steps to set up the Text Summarization Tool on your local machine.

### Prerequisites

- Python 3.10
- pip (Python package manager)

### Steps
#### Clone the Repository
    git clone https://github.com/your-username/text-summarization-tool.git
#### Create a Virtual Environment:
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
#### Install Dependencies
    pip install -r requirements.txt
#### Run the Application
    python app.py
#### Access the Tool
Open your browser and navigate to http://127.0.0.1:8080/predict.

### Usage
#### Input Text
Enter your text in the input box on the left side of the interface.
#### Generate Summary
Click the Summarize button to process the text and wait for a while.

### Technologies Used

- Python: The core programming language used for the backend.

- Flask: A lightweight web framework for building the application.

- Transformers Library: Used to load and run the google/pegasus-cnn_dailymail model.

- HTML/CSS: For the frontend interface.

Enjoy summarizing your texts with the Text Summarization Tool! 🚀

### Define the workflows

1. config.yaml
2. Params.yaml
3. Config.entity
4. Configuration manager
5. Update the components - Data Ingestion,Data Transformation, Model Trainer
6. Create our Pipeline - Training Pipeline,prediction Pipeline
7. Front end apis', Training APi's, Batch Predcition api's



