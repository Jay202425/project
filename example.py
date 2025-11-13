"""
Example usage of the OpenAI chatbot
This demonstrates how to use the bot programmatically
"""

from bot import chat_with_bot

# Example 1: Simple question
print("Example 1: Simple question")
print("-" * 50)
response = chat_with_bot("What is Python?")
print(f"User: What is Python?")
print(f"Bot: {response}\n")

# Example 2: Another question
print("Example 2: Code-related question")
print("-" * 50)
response = chat_with_bot("What are the benefits of using environment variables?")
print(f"User: What are the benefits of using environment variables?")
print(f"Bot: {response}\n")

print("=" * 50)
print("To run the interactive chatbot, use: python bot.py")
print("=" * 50)
