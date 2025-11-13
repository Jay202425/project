# OpenAI Chatbot Project

A simple chatbot implementation using OpenAI's API with secure API key management.

## Features

- Interactive chat interface using OpenAI's GPT models
- Secure API key management using environment variables
- Easy to configure and extend

## Setup

### Prerequisites

- Python 3.7 or higher
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd project
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your OpenAI API key:
   - Copy `.env.example` to `.env`
   - Replace `your_openai_api_key_here` with your actual OpenAI API key
   
```bash
cp .env.example .env
# Edit .env and add your API key
```

## Usage

Run the chatbot:

```bash
python bot.py
```

The bot will start an interactive session where you can type messages and receive responses from the AI.

Type `quit` or `exit` to end the conversation.

## Project Structure

```
.
├── bot.py              # Main chatbot application
├── .env                # Environment variables (contains API key - not committed)
├── .env.example        # Example environment file
├── requirements.txt    # Python dependencies
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## Security

⚠️ **Important**: Never commit your `.env` file to version control. The `.env` file is listed in `.gitignore` to prevent accidental commits of your API key.

## Configuration

The bot uses the following environment variables (defined in `.env`):

- `OPENAI_API_KEY`: Your OpenAI API key

## Example

```
OpenAI Chatbot
==================================================
Type 'quit' or 'exit' to end the conversation
==================================================

You: Hello!
Bot: Hello! How can I assist you today?

You: What's the weather like?
Bot: I don't have access to real-time weather data, but I'd be happy to help you with other questions!

You: exit
Goodbye!
```

## License

This project is open source and available for educational purposes.
