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
    python3 ./honeyBOT/bee/generate_person.py
done

# generate image of person
echo "Beginning image generation..."
python3 ./honeyBOT/bee/generate_image.py

# add user accounts to target system
echo "Adding honeyBOTs to target system..."
python3 ./honeyBOT/hive/add_users.py $server