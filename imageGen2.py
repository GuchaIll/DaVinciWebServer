from diffusers import DiffusionPipeline
import torch

class generateImageModel:
    def __init__(self):
    #stabilityai/stable-diffusion-xl-base-1.0
    #CompVis/stable-diffusion-v1-4
        self.pipe = DiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-xl-base-1.0", torch_dtype=torch.float16, use_safetensors=True, variant="fp16")
        self.pipe.to("cuda")
        
    def generate_image(self, prompt):
    
        images = self.pipe(prompt=prompt).images[0]