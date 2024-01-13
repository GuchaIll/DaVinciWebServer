
from openai import OpenAI

class generateImageModel:
    def __init__(self):
        self.client = OpenAI()

    def generate_image(self, prompt):
      
        client = OpenAI()

        response = client.images.generate(
        model="dall-e-3",
        prompt = prompt,
        size="1024x1024",
        quality="standard",
        n=1,
        )