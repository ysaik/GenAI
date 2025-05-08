'''
This script passed pdf files to the AI model and
queries the model with the generated prompt.
'''
from ai_utils.prompt_generator import PromptGenerator
from ai_utils.llm import LLM
from ai_utils.response_parser import AIResponseParser as RS


def process_pdf():
    # Create an instance of PromptGenerator
    prompt_generator = PromptGenerator()

    # Generate the prompt
    prompt = prompt_generator.generate(
        instructions="""
    Analyse the pdf file. understand the content.
    """,
        user_context="Answer specific to the PDF document.",
        query="""Explain Transformer architecture."""
    )

    # Create an instance of LLM
    llm = LLM()

    # Initialize the model
    llm.initialize()

    # Load PDF files
    pdf_file = "/home/saiky/GenAI-course/genai-principles.pdf"
    mime_type = "application/pdf"

    pdf_data = llm.load_files(pdf_file, mime_type)
    contents = [pdf_data, prompt]
    response = llm.ask(contents)
    generated_text = RS(response).get_text()
    print(f"Response from {pdf_file}: {generated_text}")


if __name__ == "__main__":
    process_pdf()
