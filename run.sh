#!/bin/bash

# prettify arguments:
count=$1
server=$2



# make sure we're using the right packages!
source .venv/bin/activate

# generate person
for _ in $(eval echo "{1..$count}")
do
    echo "Generating honeyBOT.."
    python3 generate_person.py
done

# generate image of person
echo "Beginning image generation..."
python3 generate_image.py

# add user accounts to target system
echo "Adding honeyBOTs to target system..."
python3 add_users.py $server

# TODO: run Auto-GPT and have a bot select a login json from the output folder, then attempt to log in with the provided username and each of the provided passwords, then log the results to a file. 

# cd Auto-GPT && docker-compose run --rm auto-gpt # at this point you'll need to do SOME intervention but eventually i'll automate it
