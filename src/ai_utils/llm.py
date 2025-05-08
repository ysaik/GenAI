'''
This module provides a function to query an AI model
using the GenerativeModel class from the vertexai.
generative_models module.'''

import vertexai
from typing import Optional
from vertexai.generative_models import GenerativeModel, Part


class LLM:
    def __init__(self,
                 project_id="mygenai-457902",
                 location="us-central1",
                 model_name="gemini-2.0-flash-001"):
        self.project_id = project_id
        self.location = location
        self.model_name = model_name
        self.model = None

    def is_local_path(self, path_string: Optional[str]) -> bool:
        if not path_string or not isinstance(path_string, str):
            return False

        non_local_schemes = ("gs://", "s3://", "https://", "http://")
        if path_string.lower().startswith(non_local_schemes):
            return False

        if path_string.startswith('/'):
            return True
        return True

    def initialize(self):
        vertexai.init(project=self.project_id, location=self.location)
        self.model = GenerativeModel(model_name=self.model_name)

    def chat_mode(self, contents):
        chat_session = self.model.start_chat()
        # Updated to use the correct argument name for send_message
        response = chat_session.send_message(contents)
        return response

    def load_files(self, file, mime_type=None):
        if not self.model:
            raise ValueError(
                "Model is not initialized. Call initialize() first.")
        if self.is_local_path(file):
            with open(file, "rb") as f:
                file_data = f.read()
            return Part.from_data(data=file_data, mime_type=mime_type)
        else:
            return Part.from_uri(file, mime_type=mime_type)

    def ask(self, contents, stream=False, chat=False):
        response = None
        if not self.model:
            raise ValueError(
                "Model is not initialized. Call initialize() first.")
        print(f"Querying: {self.model_name}")
        if chat:
            return self.chat_mode(contents)
        else:
            response = self.model.generate_content(
                contents=contents,
                stream=stream)
            if stream:
                print("Streaming response:")
                for chunk in response:
                    try:
                        print(chunk.text, end="")
                    except ValueError:
                        print("[Received chunk without text content]", end="")
        return response
