import webuiapi
import json
import os

OUTPUT_DIRECTORY = os.path.join(os.getcwd(), "output")


api = webuiapi.WebUIApi(port=7861) # --nowebui uses 7861, --api uses 7860

for person in os.listdir(OUTPUT_DIRECTORY):
    if person[0] != '.':
        with open(f"{OUTPUT_DIRECTORY}/{person}/biography.json", "r") as biography:
            biography_dict = json.load(biography)
            selfie = api.txt2img(prompt=f"close up, 1 ((upper body selfie)) adult {biography_dict['Age']} years old, {biography_dict['Ethnicity']} {biography_dict['Nationality']} {biography_dict['Gender']}, {biography_dict['Hair Color']} {biography_dict['Hair Style']} hair, BREAK {biography_dict['Eye Color']} Eyes, BREAK {biography_dict['Body Shape']} body, wearing {biography_dict['Favorite Color']} business suit, soft smile, BREAK photo of, upper body, best quality, ultra-detailed, [analog style, dslr] (look at viewer:1.2) (skin texture) (film grain:1.1), (warm hue, warm tone:1.2), ultra high res, best shadow, RAW, realistic, photorealistic,  BREAK indoors, blank walls, simple background", negative_prompt="BadDream, (UnrealisticDream:1.2), hands, (iphone:1.1), (nsfw), cleavage, extra limbs, amputee", cfg_scale=10, sampler_index="DPM++ SDE Karras", width=540, height=960, steps=35, enable_hr=True, denoising_strength=0.55,hr_second_pass_steps=35, hr_scale=2, restore_faces=True, hr_upscaler="R-ESRGAN 4x+", alwayson_scripts={"ADetailer": {"args": [True, {"ad_model": "person_yolov8n-seg.pt", "ad_restore_face": True, "ad_steps": 35}]}})
            filename = f"{OUTPUT_DIRECTORY}/{person}/photo.png"
            selfie.image.save(filename, "PNG")
            print(f"Generating {person} done!")
