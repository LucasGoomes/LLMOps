# Large Language Models Operations (LLMOps)

The LLMOps repository provides Python code for applying Large Language Models (LLMs) Operations using the Google Cloud Platform. The provided scripts demonstrate various operations such as data preparation, automation pipeline, reusing a pipeline, deployment, and inference.

## Data Preparation

The code retrieves data from a public dataset of Stack Overflow questions and answers using the BigQuery API. It then processes the data to prepare it for fine-tuning a large language model. This involves steps such as joining tables, adding instructions to the data, splitting the data into training and evaluation sets, and versioning the data for reproducibility.

## Automation Pipeline

The scripts showcase how to automate and orchestrate a sequence of operations using Kubeflow Pipelines. It demonstrates the creation of a simple pipeline that executes a sequence of tasks. It also includes an example of reusing an existing pipeline for Parameter-Efficient Fine-Tuning of a foundation model from Google.

## Deployment

The code includes examples of deploying a trained model for both batch and real-time processing. It also demonstrates how to perform inference using the deployed model and manage prompts for the model.

## Safety Attributes and Citations

The response from the LLM includes safety scores that can be used to ensure the model's response is within the expected behavior bounds. It also includes citation metadata that can be used to check and reduce the chances of the model generating a lot of existing content.
