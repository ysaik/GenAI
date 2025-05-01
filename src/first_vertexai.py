"""
This program is to demonstrate the use of the Vertex
AI Generative Model API.`
"""
from ai_utils.llm import LLM
from ai_utils.response_parser import AIResponseParser as RS


def run_ai_query():

    # Create an instance of AIQuery
    llm = LLM()

    # Initialize the model
    llm.initialize()

    # Query the model with the generated prompt
    response = llm.ask("Who is the Prime Minister of India?")
    RS(response).dump_response()

# Call the function


if __name__ == "__main__":
    run_ai_query()
