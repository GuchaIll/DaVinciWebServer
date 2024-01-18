import PIL.Image
import PIL.ImageOps
import requests
import torch
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler
import matplotlib.pyplot as plt
import numpy as np

class modifyImageModel:
    def __init__(self):

        model_id = "timbrooks/instruct-pix2pix"
        self.pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(model_id, torch_dtype=torch.float16, safety_checker=None)
        self.pipe.to("cuda")
        self.pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(self.pipe.scheduler.config)
      
        #url = "https://raw.githubusercontent.com/timothybrooks/instruct-pix2pix/main/imgs/example.jpg"
    def download_image(url):
        image = PIL.Image.open(requests.get(url, stream=True).raw)
        image = PIL.ImageOps.exif_transpose(image)
        image = image.convert("RGB")
        return image
    
    def modify_image(self, src, prompt):
        #image = self.download_image(url)
        
        image = PIL.Image.open(src)
        images = self.pipe(prompt, image=image, num_inference_steps=10, image_guidance_scale=1).images


        # Assuming images[0] is the output image
        output_image = images[0]
        
        return output_image