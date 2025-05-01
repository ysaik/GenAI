'''
This module provides a function to query an AI model
using the GenerativeModel class from the vertexai.
generative_models module.'''

import vertexai
from vertexai.generative_models import GenerativeModel


class LLM:
    def __init__(self,
                 project_id="mygenai-457902",
                 location="us-central1",
                 model_name="gemini-2.0-flash-001"):
        self.project_id = project_id
        self.location = location
        self.model_name = model_name
        self.model = None

    def initialize(self):
        vertexai.init(project=self.project_id, location=self.location)
        self.model = GenerativeModel(model_name=self.model_name)

    def ask(self, contents):
        if not self.model:
            raise ValueError(
                "Model is not initialized. Call initialize() first.")
        print(f"Querying: {self.model_name}")
        response = self.model.generate_content(contents=contents)
        return response
