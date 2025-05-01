'''
This script demonstrates how to use the Vertex AI API
to query a model with a generated prompt.
'''
from ai_utils.prompt_generator import PromptGenerator
from ai_utils.llm import LLM
from ai_utils.response_parser import AIResponseParser as RS


def run_ai_query():
    # Create an instance of PromptGenerator
    prompt_generator = PromptGenerator()

    # Generate the prompt
    prompt = prompt_generator.generate(
        instructions="Answer the following question concisely.",
        user_context="The user is asking about political leaders.",
        query="Who is the Prime Minister of India?"
    )

    # Create an instance of AIQuery
    llm = LLM()

    # Initialize the model
    llm.initialize()

    # Query the model with the generated prompt
    response = llm.ask(prompt)
    RS(response).dump_response()


# Call the function
if __name__ == "__main__":
    run_ai_query()
