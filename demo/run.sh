#!/bin/bash

# prettify arguments:
count=$1
server=$2

head -n 6 ../.honeybot.txt 

# make sure we're using the right packages!
source ../.venv/bin/activate

# generate person
for _ in $(eval echo "{1..$count}")
do
    echo "Generating honeyBOT..."
    python3 generate_person.py
done

# generate image of person
#echo "Beginning image generation..."
#python3 generate_image.py

# generate social media posts
echo "Generating social media posts..."
python3 generate_posts.py

# add user accounts to target system
echo "Adding honeyBOTs to target system..."
python3 add_users.py $server

# mkdir -p ./Auto-GPT/autogpt/auto_gpt_workspace/output
# cp -R ./output/ ./Auto-GPT/autogpt/auto_gpt_workspace/output

#  # TODO: run Auto-GPT and have a bot select a login json from the output folder, then attempt to log in with the provided username and each of the provided passwords, then log the results to a file. 
# echo "Running Auto-GPT, time for you to take over!s"
# cd Auto-GPT && docker-compose run --rm auto-gpt # at this point you'll need to do SOME intervention but eventually i'll automate it
