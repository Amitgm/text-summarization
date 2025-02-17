# text-summarization using Hugginng face

# TEXT-SUMMARIZATION TOOL

The Text Summarization Tool is a powerful application that uses the google/pegasus-cnn_dailymail model to generate concise and accurate summaries of input texts. Built with Flask and Python, this tool leverages a fine-tuned Seq2Seq model to provide high-quality summaries for long articles, documents, or any text input.

## Features

- State-of-the-Art Model: Utilizes the google/pegasus-cnn_dailymail model, a pre-trained Seq2Seq model fine-tuned for summarization tasks.

- User-Friendly Interface: A clean and intuitive web interface with an input text box and a summary output box.

- Fast and Efficient: Summarizes text in real-time with minimal latency.

- Customizable: Easily extendable for additional features or integration with other tools.

## Model Details

- Model Name: google/pegasus-cnn_dailymail

- Architecture: Seq2Seq (Transformer-based)

- Fine-Tuning: Fine-tuned on the cnn_dailymail dataset for optimal summarization performance.

### How It Works

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






### Define the workflows

1. config.yaml
2. Params.yaml
3. Config.entity
4. Configuration manager
5. Update the components - Data Ingestion,Data Transformation, Model Trainer
6. Create our Pipeline - Training Pipeline,prediction Pipeline
7. Front end apis', Training APi's, Batch Predcition api's



