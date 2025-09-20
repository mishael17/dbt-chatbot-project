from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

load_dotenv()
gemini_api_key = os.getenv('gemini_api_key')

class LLMClient:

    def __init__(self):
        self.client = genai.Client(api_key=gemini_api_key)

    def generate_content(self, model: str, contents):
        response = self.client.models.generate_content(
            model=model,
            contents=contents
        )
        return response
"""
# Usage Example
if __name__ == "__main__":
    client = LLMClient()

    contents=[
            types.Content(
                role="user",
                parts=[
                    types.Part(
                        text="You are a travel expert.Here is some information:"
						"A plan to go to Greece in winter this year"
                        "How plan a good adventurous experience"

                    )
                ]
            )
        ]



    response = client.generate_content(
        model="gemini-2.5-flash",
        contents=contents
    )

    print(response.text)





"""


