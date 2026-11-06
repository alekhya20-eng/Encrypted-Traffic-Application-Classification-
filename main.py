import os
from dotenv import load_dotenv from openai import OpenAI
# Load API key load_dotenv()
api_key = os.getenv("OPENAI_API_KEY") # Initialize client
client = OpenAI(api_key=api_key) # Send request
response = client.chat.completions.create( model="gpt-4.1-mini",
messages=[{"role": "user", "content": "Hello"}]
)
# Print response 