"""Python script to test Google GenAI API with a simple query."""
# Import necessary libraries
from google import genai
from google.genai.types import HttpOptions

client = genai.Client(http_options=HttpOptions(api_version="v1"))
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents="Who is the Prime Minister of India?",
)
print(response.text)
