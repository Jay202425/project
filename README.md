# OpenAI Chatbot Project

A chatbot implementation using OpenAI's API with both command-line and web interfaces.

## Features

- 🌐 **Web Interface**: Modern Streamlit-based chat UI
- 💻 **Command-Line Interface**: Traditional terminal-based chatbot
- 🔒 **Secure API Key Management**: Environment variables and Streamlit secrets
- 💬 **Conversation History**: Persistent chat history in web interface
- ⚡ **Streaming Responses**: Real-time response generation

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

**For command-line usage:**
   - Copy `.env.example` to `.env`
   - Replace `your_openai_api_key_here` with your actual OpenAI API key
   
```bash
cp .env.example .env
# Edit .env and add your API key
```

**For Streamlit deployment:**
   - Add your API key to Streamlit secrets (for cloud deployment)
   - Or use the `.env` file for local Streamlit runs

## Usage

### Web Interface (Streamlit)

Run the Streamlit app:

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

**For Streamlit Cloud deployment:**
1. Deploy your repository to Streamlit Cloud
2. Add `OPENAI_API_KEY` to your app's secrets in the Streamlit Cloud dashboard
3. Your app will be available at your Streamlit Cloud URL

### Command-Line Interface

Run the chatbot:

```bash
python bot.py
```

The bot will start an interactive session where you can type messages and receive responses from the AI.

Type `quit` or `exit` to end the conversation.

## Project Structure

```
.
├── app.py                      # Streamlit web application
├── bot.py                      # Command-line chatbot
├── example.py                  # Usage examples
├── test_config.py              # Configuration tests
├── .env                        # Environment variables (not committed)
├── .env.example                # Example environment file
├── .streamlit/
│   ├── config.toml            # Streamlit configuration
│   └── secrets.toml.example   # Example secrets file
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore file
└── README.md                  # This file
```

## Security

⚠️ **Important**: Never commit your `.env` file or `.streamlit/secrets.toml` to version control. These files are listed in `.gitignore` to prevent accidental commits of your API key.

## Configuration

The bot uses the following environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key

**Local development:**
- Store in `.env` file (loaded by python-dotenv)

**Streamlit Cloud deployment:**
- Add to app secrets in Streamlit Cloud dashboard
- Settings → Secrets → Add secret: `OPENAI_API_KEY = "your-key-here"`

## Examples

### Command-Line Interface

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

### Web Interface

The Streamlit app provides:
- Clean, modern chat interface
- Real-time streaming responses
- Conversation history
- Clear chat button
- Status indicators

## Troubleshooting

### Streamlit App Not Running

1. **API Key Not Configured:**
   - For local: Ensure `.env` file exists with `OPENAI_API_KEY`
   - For Streamlit Cloud: Add API key to app secrets in dashboard

2. **Dependencies Not Installed:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Port Already in Use:**
   ```bash
   streamlit run app.py --server.port 8502
   ```

## License

This project is open source and available for educational purposes.
