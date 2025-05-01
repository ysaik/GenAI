'''
Prompt Generator Module
This module provides a class to generate
prompts based on a Jinja2 template.
'''
import os
from jinja2 import Template


class PromptGenerator:
    """
    A class to generate prompts based on a Jinja2 template.
    """

    def __init__(self, template_path="templates/prompt.j2.txt"):
        self.template_path = template_path

    def generate(self, instructions, user_context, query, notes=None):
        """
        Populates the prompt template with the given inputs.

        Args:
            instructions (str): The task instructions.
            user_context (str): Background or context provided by the user.
            query (str): The problem statement or query.
            notes (str, optional): Additional notes, if any.

        Returns:
            str: The populated template.
        """
        if not os.path.exists(self.template_path):
            raise FileNotFoundError(
                f"Template file '{self.template_path}' not found.")

        with open(self.template_path, "r") as file:
            template_content = file.read()

        template = Template(template_content)
        populated_template = template.render(
            instructions=instructions,
            user_context=user_context,
            query=query,
            notes=notes
        )
        return populated_template
