# Profaid Model

## Overview
The Profaid Model is a machine learning model designed to predict whether a student or an AI authors a text. This repository also includes a Flask-based microservice allowing users to make local predictions.

## Table of Contents
1. Installation
2. Usage
3. Microservice
4. Contributing

## Installation
To use the Profaid Model, follow these steps:

## Clone the repository to your local machine:
1. `git clone https://github.com/your-username/Profaid-Model.git`
2. `cd Profaid-Model`

#3 Install the required dependencies:
pip install -r requirements.txt
Download the pre-trained model weights (if available) or train the model using the instructions in the Model Training section.

## Usage
You can use the Profaid Model in your Python code by importing the necessary functions from the profaid_model module.

## Microservice
The repository includes a Flask-based microservice that allows you to make predictions locally. To run the microservice, follow these steps:

### 1. Ensure you have the required dependencies installed:
`pip install ALL_REQUIREMENTS`

### 2. Start the Flask app:
python app.py
The microservice will be accessible at `http://127.0.0.1:5000/predict?text=your_input_data_here`. You can use this endpoint to make predictions using the provided API.

## Contributing
If you would like to contribute to the development of the Profaid Model, please follow the guidelines in CONTRIBUTING.md.
