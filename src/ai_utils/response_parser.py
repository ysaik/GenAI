'''
Parse the AI response and getter functions to get each value
json

{
  "candidates": [
    {
      "avg_logprobs": -0.018483588641340084,
      "content": {
        "parts": [
          {
            "text": "The current Prime Minister of India is Narendra Modi.\n"
          }
        ],
        "role": "model"
      },
      "finish_reason": "STOP"
    }
  ],
  "create_time": "2025-05-01T14:23:17.419503Z",
  "model_version": "gemini-2.0-flash-001",
  "response_id": "1YMTaK_NGYyDqsMPqp2B-Ac",
  "usage_metadata": {
    "candidates_token_count": 11,
    "candidates_tokens_details": [
      {
        "modality": "TEXT",
        "token_count": 11
      }
    ],
    "prompt_token_count": 8,
    "prompt_tokens_details": [
      {
        "modality": "TEXT",
        "token_count": 8
      }
    ],
    "total_token_count": 19
  }
}
'''
import json


class AIResponseParser:
    """
    A class to parse and handle AI responses.
    """

    def __init__(self, response):
        """
        Initialize the parser with the AI response.

        Args:
            response: The AI response object.
        """
        self.response = response

    def dump_response(self):
        """
        Dumps the response from the AI into a structured format.
        """
        jstr = json.dumps(self.response.to_dict(), sort_keys=2, indent=2)
        print(jstr)

    def get_text(self):
        """
        Dumps the text content from the AI response.
        """
        return self.response.candidates[0].content.parts[0].text

    def get_avg_logprobs(self):
        """
        Get the average log probabilities from the response.
        """
        return self.response.candidates[0].avg_logprobs

    def get_finish_reason(self):
        """
        Get the finish reason from the response.
        """
        return self.response.candidates[0].finish_reason

    def get_model_version(self):
        """
        Get the model version from the response.
        """
        return self.response.model_version

    def get_response_id(self):
        """
        Get the response ID from the response.
        """
        return self.response.response_id

    def get_create_time(self):
        """
        Get the creation time of the response.
        """
        return self.response.create_time

    def get_total_token_count(self):
        """
        Get the total token count from the response.
        """
        return self.response.usage_metadata.total_token_count

    def get_prompt_token_count(self):
        """
        Get the prompt token count from the response.
        """
        return self.response.usage_metadata.prompt_token_count

    def get_candidates_token_count(self):
        """
        Get the candidates token count from the response.
        """
        return self.response.usage_metadata.candidates_token_count
