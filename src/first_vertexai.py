"""
This program is to demonstrate the use of the Vertex
AI Generative Model API.`
"""
import vertexai
from vertexai.generative_models import GenerativeModel

PROJECT_ID = "mygenai-457902"
LOCATION = "us-central1"
MODEL_NAME = "gemini-2.0-flash-001"

vertexai.init(project=PROJECT_ID, location=LOCATION)

model = GenerativeModel(MODEL_NAME)
user_input = input("Mr. LLM: Ask your query!! or 'quit' to exit: \nYou: ")
while True:
    # Generate content using the model
    response = model.generate_content(user_input)
    generated_text = response.candidates[0].content.parts[0].text
    print("Mr LLM : "+generated_text)

    # Get user input
    user_input = input("You : ")
    if user_input.lower() == "quit":
        break
