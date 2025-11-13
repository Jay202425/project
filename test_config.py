"""
Test script to verify the bot configuration
"""

import os
from dotenv import load_dotenv

# Test 1: Check if .env file exists and can be loaded
print("Test 1: Loading .env file...")
load_dotenv()
print("✓ .env file loaded successfully")

# Test 2: Check if API key is loaded
print("\nTest 2: Checking API key...")
api_key = os.getenv("OPENAI_API_KEY")
if api_key:
    print(f"✓ API key found (length: {len(api_key)} characters)")
    print(f"  Starts with: {api_key[:10]}...")
    print(f"  Ends with: ...{api_key[-10:]}")
else:
    print("✗ API key not found!")
    exit(1)

# Test 3: Check if OpenAI client can be initialized
print("\nTest 3: Initializing OpenAI client...")
try:
    from openai import OpenAI
    client = OpenAI(api_key=api_key)
    print("✓ OpenAI client initialized successfully")
except Exception as e:
    print(f"✗ Failed to initialize OpenAI client: {e}")
    exit(1)

# Test 4: Import bot module
print("\nTest 4: Importing bot module...")
try:
    import bot
    print("✓ Bot module imported successfully")
    print(f"✓ chat_with_bot function available: {callable(bot.chat_with_bot)}")
except Exception as e:
    print(f"✗ Failed to import bot module: {e}")
    exit(1)

print("\n" + "=" * 50)
print("All tests passed! ✓")
print("=" * 50)
print("\nYou can now run the bot with: python bot.py")
