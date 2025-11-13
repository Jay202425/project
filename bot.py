"""
OpenAI Bot - A simple chatbot using OpenAI's API

This bot demonstrates basic integration with OpenAI's chat completion API.
The API key is securely stored in a .env file.
"""

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI client with API key from environment
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY not found in environment variables. Please check your .env file.")

client = OpenAI(api_key=api_key)


def chat_with_bot(user_message, model="gpt-3.5-turbo"):
    """
    Send a message to the OpenAI bot and get a response.
    
    Args:
        user_message (str): The message from the user
        model (str): The OpenAI model to use (default: gpt-3.5-turbo)
    
    Returns:
        str: The bot's response
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_message}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"


def main():
    """
    Main function to run the interactive chatbot.
    """
    print("OpenAI Chatbot")
    print("=" * 50)
    print("Type 'quit' or 'exit' to end the conversation")
    print("=" * 50)
    print()
    
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check for exit commands
        if user_input.lower() in ['quit', 'exit']:
            print("Goodbye!")
            break
        
        # Skip empty inputs
        if not user_input:
            continue
        
        # Get bot response
        print("Bot: ", end="", flush=True)
        response = chat_with_bot(user_input)
        print(response)
        print()


if __name__ == "__main__":
    main()
