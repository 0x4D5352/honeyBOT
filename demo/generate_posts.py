"""
This script will take the input from the biography file, search the internet for some current events, and generate a post for each event based on the biography.
The first iteration of this script won't directly post to social media, but will generate the posts and save them to a file.
We loop through the people in the output directory's subdirectories, and generate three posts for each person.
Each post will be based on the person's biography, which is found in a text file titled summary.txt.
This first iteration will be generic and not take into account current events, only the biography.
The posts will be output into a text file, with each post separated by a newline.
"""

import gpt4all
# import json
from pathlib import Path

MODEL_DIRECTORY = Path('../gpt4all/models')
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


# setting up the LLM
gptj = gpt4all.GPT4All(model_name=LARGE_LANGUAGE_MODEL, model_path=str(MODEL_DIRECTORY))

# helper function
def generate_response(chat_history):
    return gptj.chat_completion(messages=chat_history, default_prompt_header=False, verbose=DISPLAY_CHAT, streaming=False, temp=TEMP, n_ctx=N_CTX, n_predict=N_PREDICT, n_batch=N_BATCH, top_k=TOP_K, top_p=TOP_P, repeat_penalty=REPEAT_PENALTY)

# loop through each person in the output directory
for person in Path('output').iterdir():
    person_directory = Path(person)
    if person_directory.exists() and person_directory.is_dir():
        # open the biography file and read the contents
        with open(Path(person_directory, "summary.txt"), "r") as f:
            biography_text = f.read()
            # generate the prompt
            prompt = [
                {"role": "system", "content": "### Instruction:\nYou are the person described in the following biograhy summary."},
                {"role": "system", "content": "Biography Summary:\n"},
                {"role": "system", "content": f"{biography_text}"},
                {"role": "system", "content": "The user will request a post about a current event. You will respond to the request with one or more posts about the event based on your background: Your cultural background, your astrological sign, etc."},
                {"role": "system", "content": "Reference the people, places, and additional details in the biography summary when generating your responses."},
                {"role": "system", "content": "If the user requests multiple posts, your response should countain each post separated by a semicolon."},
                {"role": "system", "content": "Your response should contain only the posts, and no additional commentary or information."},
                {"role": "user", "content": "### Prompt:\nWrite three posts about going out to dinner with your family."}
            ]
            # generate the response
            response = generate_response(prompt)["choices"][0]["message"]["content"].strip()
            # print the response
            print(response)
            # save the response to a file in the person's directory named "posts.txt"
            with open(Path(person_directory, "posts.txt"), "w") as f:
                f.write(response)
