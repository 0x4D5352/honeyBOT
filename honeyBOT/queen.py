from . import queen

"""
The queen module is the main module of honeyBOT, and has three main responsibilities:
1. Generate the drones' backstory with an LLM, which involves:
    1a. Generating a biography for each drone.
    1b. Summarizing the biography into a single paragraph for the user to read.
    1c. Creating a user account name and a set of insecure passwords for the drone based on their biography.
2. Generate the drones' profile picture with a Stable Diffusion model, which involves:
    2a. Taking details from the biography and using them to generate a prompt for the model.
    2b. Use the prompt to generate a 1080x1920 image of the drone.
    2c. Use img2mg to generate variations of the image to try and keep the same face.
3. Generate system interactions with the drones, which involves:
    3a. Creating a user account for the drone on the server.
    3b. Using AutoGPT to generate actions for the drone to take.
"""