# Smarcomms Facebook Bot

## Introduction
This project aims to develop a Facebook bot capable of resolving user queries related to Smarcomms using AI-powered responses generated by OpenAI models using RAG (Retrieval-Augmented Generation) process. The objective is to provide an efficient and interactive solution for handling user inquiries about Smarcomms services.

## Getting Started
To run the Smarcomms Facebook bot on your own system, follow these steps:

1. **Installation Process:**
   - Ensure you have Python installed, preferably version 3.10.
   - Create a virtual environment for the project:
     ```bash
     python3.10 -m venv ./venv
     ```
   - Activate the virtual environment:
     ```bash
     source ./venv/bin/activate
     ```
   - Upgrade pip:
     ```bash
     pip install --upgrade pip
     ```
   - Install dependencies listed in `requirements.txt`:
     ```bash
     pip install -r requirements.txt
     ```

2. **Setup .env File:**
   - Create a `.env` file in the root directory of the project.
   - Use the `.env.example` file included in the code as a reference to set up your environment variables.
   - Ensure to include necessary credentials and configuration details such as Facebook API keys, OpenAI API keys, etc.

3. **Training the Model:**
   - After installing dependencies, train the Rasa model:
     ```bash
     rasa train
     ```

4. **Starting Servers:**
   - Once the model is trained, you can start the servers by running the `start.sh` file included in the code:
     ```bash
     sh start.sh
     ```

With these steps completed, your Smarcomms Facebook bot should be up and running, ready to handle user queries effectively.

For more detailed API references and documentation, please refer to the official Rasa documentation.
https://rasa.com/

## Dependencies
- Python 3.10
- Rasa Bot-framework
- OpenAI models (Chat Completion Model and Text Embedding Model)

## Setting up Facebook Developer App
- Ensure to set up a Facebook Developer App to obtain necessary access tokens and credentials required for integrating your bot with Facebook Messenger.
- Follow the documentation provided by Facebook for creating a new app and configuring Messenger settings.
- Obtain necessary tokens and credentials and update them in your `.env` file.

## Repo Structure
- **actions:** This directory contains all custom action files and logic responsible for generating responses.
- **common:** This section stores all constants utilized throughout the project.
- **config:** Here, you'll find settings or credentials essential for the project's operation.
- **data:** This section encompasses the NLU (Natural Language Understanding) module, includes intents and rules that describes the workflow of the bot.
- **dataset:** This directory includes embeddings utilized in the project.
- **services:** Here, you'll find all the business logic that operates on the data.
- **config.yaml:** This file outlines the pipeline structure necessary for model creation as well as for the intent detections.
- **domain:** This section registers all actions and intents used by the bot.
- **endpoint:** This directory contains the endpoint for the action server, facilitating connectivity with our bot.

---
