import os
from dotenv import load_dotenv
from octoai.clients.image_gen import Engine, ImageGenerator
    
load_dotenv()

def get_image():
    image_gen = ImageGenerator(token=os.getenv("OCTOAI_API_TOKEN"))
    image_gen_response = image_gen.generate(
        engine=Engine.SDXL,
        prompt="An drink in the center with a vodka liquor bottle next to it",
        negative_prompt="Blurry photo, distortion, low-res, poor quality",
        width=1536,
        height=640,
        num_images=1,
        sampler="LCM",
        steps=6,
        cfg_scale=1.4,
        use_refiner=False,
        style_preset="Watercolor",
    )
    images = image_gen_response.images

    for i, image in enumerate(images):
        image.to_file(f"result{i}.jpg")