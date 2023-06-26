import gpt4all
import json
import os
from datetime import date
from secrets import randbelow
from time import time

# models = [model["filename"] for model in gpt4all.GPT4All.list_models()]
# ! if you run into any issues, use this to see the different models and pick the best one

WORKING_DIRECTORY = os.getcwd()
LARGE_LANGUAGE_MODEL = "ggml-nous-gpt4-vicuna-13b.bin" # best working model as of implementation deadline, can be improved.
DISPLAY_CHAT = False # change to True to see the output as it prints. Useful for debugging.

# LLM Parameters

# randomness/reptition controls
TEMP = .99 # controls how random the output is gonna be, .1 is default
TOP_K = 80 # number of possible choices, 40 is default
TOP_P = 5.0 # threshold for accepted choices, .9 is default
REPEAT_PENALTY = 1.2 # bias against repetition, 1.2 is default

# if your computer performance suffers, halve/quarter these values
N_CTX = 2048  # context window for tokens, 1024 is default
N_PREDICT = 256 # token generation limit, 128 is default
N_BATCH = 16 # tokens processed per prompt, 8 is default

# TODO: parameterize all the things so that you can turn this into a library thats' imported into __main__

# TODO: convert the prompts to config files
# prompts for the LLM
PROMPTS = [{"role": "user", "content": "### Prompt:\nGender:"}, 
           {"role": "user", "content": "### Prompt:\nEthnicity:"}, 
           {"role": "user", "content": "### Prompt:\nNationality:"}, 
           {"role": "user", "content": "### Prompt:\nPlace Of Birth:"}, 
           {"role": "user", "content": "### Prompt:\nDate Of Birth:"}, 
           {"role": "user", "content": "### Prompt:\nAstrological Sign:"}, 
           {"role": "user", "content": "### Prompt:\nAge:"}, 
           {"role": "user", "content": "### Prompt:\nLast Name:"}, 
           {"role": "user", "content": "### Prompt:\nFirst Name:"}, 
           {"role": "user", "content": "### Prompt:\nMiddle Name:"}, 
           {"role": "user", "content": "### Prompt:\nStreet Address:"}, 
           {"role": "user", "content": "### Prompt:\nCity of Residence:"}, 
           {"role": "user", "content": "### Prompt:\nTelephone Number:"}, 
           {"role": "user", "content": "### Prompt:\nEducational Bacgkround:"}, 
           {"role": "user", "content": "### Prompt:\nEmail Address:"}, 
           {"role": "user", "content": "### Prompt:\nFather's First Name:"}, 
           {"role": "user", "content": "### Prompt:\nMother's First Name:"}, 
           {"role": "user", "content": "### Prompt:\nMother's Maiden Name:"}, 
           {"role": "user", "content": "### Prompt:\nSiblings:"}, 
           {"role": "user", "content": "### Prompt:\nHair Color:"}, 
           {"role": "user", "content": "### Prompt:\nHair Style:"}, 
           {"role": "user", "content": "### Prompt:\nEye Color:"}, 
           {"role": "user", "content": "### Prompt:\nBody Shape:"}, 
           {"role": "user", "content": "### Prompt:\nHeight:"}, 
           {"role": "user", "content": "### Prompt:\nWeight:"}, 
           {"role": "user", "content": "### Prompt:\nRelationship Status:"}, 
           {"role": "user", "content": "### Prompt:\nPartner's Name:"}, 
           {"role": "user", "content": "### Prompt:\nPet's Species:"}, 
           {"role": "user", "content": "### Prompt:\nPet's Name:"}, 
           {"role": "user", "content": "### Prompt:\nVehicle:"}, 
           {"role": "user", "content": "### Prompt:\nFavorite Color:"}, 
           {"role": "user", "content": "### Prompt:\nFavorite Food:"}, 
           {"role": "user", "content": "### Prompt:\nFavorite Book:"}, 
           {"role": "user", "content": "### Prompt:\nFavorite Sport:"}, 
           {"role": "user", "content": "### Prompt:\nFavorite TV Show:"}, 
           {"role": "user", "content": "### Prompt:\nFavorite Recent Movie:"}, 
           {"role": "user", "content": "### Prompt:\nFavorite Musical Genre:"}, 
           {"role": "user", "content": "### Prompt:\nFavorite Musician:"}, 
           {"role": "user", "content": "### Prompt:\nPersonality:"}, 
           {"role": "user", "content": "### Prompt:\nHobbies:"}]

TEMPLATE_JOBS = ["Accountant", "Project Manager", "Software Engineer", "System Administrator"]

# timestamp at start of generation
start_time = time()

# setting up the LLM
gptj = gpt4all.GPT4All(model_name=LARGE_LANGUAGE_MODEL, model_path=os.path.join(WORKING_DIRECTORY, "gpt4all/models"))

# helper function
def generate_response(chat_history):
    return gptj.chat_completion(messages=chat_history, default_prompt_header=False, verbose=DISPLAY_CHAT, streaming=False, temp=TEMP, n_ctx=N_CTX, n_predict=N_PREDICT, n_batch=N_BATCH, top_k=TOP_K, top_p=TOP_P, repeat_penalty=REPEAT_PENALTY)
      

generator = [
            {"role": "system", "content": "### Instruction:\nYou are a random character generator. Your responses should be short and direct. Responses should be one word, a sequence of digits, or a short phrase."}, 
            {"role": "system", "content": "When answering, do not provide any additional information, do not explain decisions, and keep all responses realistic."},
            {"role": "system", "content": "Answers should contain no special characters or accent markings. Use standard ASCII only."},
            {"role": "system", "content": "As an example, if the prompt is \"Eye Color:\", your response should be a single natural eye color, such as blue, green, or hazel."},
            {"role": "system", "content": "There should be an equal likelihood for male or female characters."},
            {"role": "system", "content": "The character can be of any Ethnic background."},
            {"role": "system", "content": "The character can be of any Nationality - American, Canadian, Mexican, French, Chinese, Vietnamese, Nigerian, South African, etc."},
            {"role": "system", "content": "The character's Ethnicity and Nationality can be the same, as in a French person living in France, or different, as in a Chinese person living in Australia."},
            {"role": "system", "content": "The character can live in their place of birth or another city based on their Nationality."},
            {"role": "system", "content": "The character's first name should reflect their Nationality. Their last name should reflect their Ethnicity."},
            {"role": "system", "content": "The character's sexual orientation can be Heterosexual, Bisexual, Homosexual, or Pansexual."},
            {"role": "system", "content": f"The current date is {date.today()}. The character should be approximately {randbelow(32) + 18} years old, relative to today."},
            {"role": "system", "content": "The character's date of birth should follow the format YYYY-MM-DD. For example, 2001-07-29"},
            {"role": "system", "content": "All names should be unique. If a name already appears in the chat history, choose a different name."},
            {"role": "system", "content": "The Pet's species should be a standard domesticated animal, such as a dog, cat, rabbit, snake, or ferret."},
            {"role": "system", "content": "Pet names should be quirky and reference objects, food, or celebrities. Any common nouns should be in the native language of the character's ethnicity and/or nationality."},
            {"role": "system", "content": "The character can be single, dating, engaged, married, divored, or widowed."},
            {"role": "system", "content": "Using the following formatting prompts as a template, generate a fictional character."},
            {"role": "user", "content": "### Prompt:\nOccupation:"},
            {"role": "assistant", "content": f"\n{TEMPLATE_JOBS[randbelow(len(TEMPLATE_JOBS))]}"}
            ]

biography = {}

print("Generating honeyBOT.drone:")

for prompt in PROMPTS:
   generator.append(prompt)
   key = prompt["content"][12:-1]
   responses = generate_response(generator)
   response = responses["choices"][0]["message"]
   value = response["content"].strip()
   biography[key] = value
   generator.append(response)
   if not DISPLAY_CHAT:
      print(f"{key}: {value}") # either show the full logs, or just show the output



character_name = f"{biography['First Name']}{biography['Last Name']}"
output_directory = os.path.join(WORKING_DIRECTORY, "output", character_name)
if os.path.exists(output_directory):
   generator.append({"role": "user", "content": "The name chosen already exists. Pick a new first name."})
   key = "First Name"
   value = generate_response(generator)["choices"][0]["message"]["content"].strip()
   biography[key] = value
   character_name = f"{biography['First Name']}{biography['Last Name']}"
   output_directory = os.path.join(WORKING_DIRECTORY, "output", character_name)
os.mkdir(output_directory)
with open(os.path.join(output_directory, "biography.json"), "w") as biography_file:
   json.dump(biography, biography_file)
   
print("Generating summary:")
   
summarizer = [{"role": "system", "content": "### Instruction:\nYou are a helpful assistant, skilled at reading python dictionaries and summarizing them."}, 
               {"role": "system", "content": "The prompt will be formatted as dictionary entries in the format Key: Value."}, 
               {"role": "system", "content": "Your response should be a one to three paragraph summary of the person described within the dictionary."},
               {"role": "user", "content": f"### Prompt:\n{biography}"}]

summary = generate_response(summarizer)["choices"][0]["message"]["content"].strip()
print(summary)
with open(os.path.join(output_directory, "summary.txt"), "w") as summary_file:
   summary_file.write(summary)
   
password_generator = [ {"role": "system", "content": "### Instruction:\nYou are a helpful assistant, skilled at reading python dictionaries and creating usernames and passwords."},
                        {"role": "system", "content": "Using the dictionary provided, you should create a username and three passwords based on the information described."},
                        {"role": "system", "content": "The username should follow the format of first initial, last name. For example, John Smith would have a username of jsmith."},
                        {"role": "system", "content": "The passwords should reference the person's astrological sign, family members, singificant others, pets, or interests like favorite movie/artist and hobbies."},
                        {"role": "system", "content": "The passwords should avoid referencing the person's ethnicity, sexual orientation, or physical features."},
                        {"role": "system", "content": "Each password should be between 8 and 15 alphanumeric characters, with a few letters capitalized."},
                        {"role": "system", "content": "For example, if the person's favorite movie is The Big Lebowski, one of their password could be WheresTheMoney1"},
                        {"role": "system", "content": 'Format your response as a JSON file: {"Username": "flast", "Password1": "pass1", "Password2": "pass2", "Password3": "pass3"}'},
                        {"role": "user", "content": f"### Prompt:\n{biography}"}
                        ]

password_json = generate_response(password_generator)["choices"][0]["message"]["content"].strip()
with open(os.path.join(output_directory, "logins.json"), "w") as summary_file:
   summary_file.write(password_json)
   
print(f"Done generating {character_name}! Took {(time() - start_time) // 60} minutes and {(time() - start_time) % 60} seconds.")