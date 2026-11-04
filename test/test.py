import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv(override=True)  # Load environment variables from .env file

# 1. Initialize the client
# This automatically looks for an environment variable named OPENAI_API_KEY.
# Alternatively, you can pass it directly: client = OpenAI(api_key="your-api-key-here")
client = OpenAI()

def test_openai_connection():
    print("Testing connection to OpenAI...")
    try:
        # 2. Call the Chat Completions API
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # Using a fast, cost-effective model for testing
            messages=[
                {"role": "developer", "content": "You are a helpful assistant."},
                {"role": "user", "content": "Hello! If you can read this, reply with 'Connection successful!'"}
            ],
            max_tokens=20
        )
        
        # 3. Print the response text
        print("\n--- Response Received ---")
        print(response.choices[0].message.content.strip())
        print("-------------------------")
        
    except Exception as e:
        print(f"\n❌ Connection failed! Error: {e}")

if __name__ == "__main__":
    # Optional: Quick check to ensure your API key environment variable is set
    if not os.environ.get("OPENAI_API_KEY"):
        print("⚠️ Warning: OPENAI_API_KEY environment variable not found.")
        print("Please set it in your terminal (e.g., export OPENAI_API_KEY='your_key')")
        print("or pass it directly to OpenAI(api_key='your_key') inside the script.\n")
        
    test_openai_connection()
