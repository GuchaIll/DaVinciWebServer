from diffusers import DiffusionPipeline, LCMScheduler

class generateImageModel:
    def __init__(self):
        self.pipe = DiffusionPipeline.from_pretrained("Lykon/dreamshaper-7").to("cuda") 
        self.pipe.scheduler = LCMScheduler.from_config(self.pipe.scheduler.config)
        self.pipe.load_lora_weights("latent-consistency/lcm-lora-sdv1-5") #yes, it's a normal LoRA

    def generate_image(self, prompt):
        results = self.pipe(
            prompt= prompt,
            num_inference_steps=4,
            guidance_scale=0.0,
        )
        return results.images[0]