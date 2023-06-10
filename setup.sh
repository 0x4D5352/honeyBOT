#!/bin/bash
#  _                            ____   ___ _____ 
# | |__   ___  _ __   ___ _   _| __ ) / _ \_   _|
# | '_ \ / _ \| '_ \ / _ \ | | |  _ \| | | || |  
# | | | | (_) | | | |  __/ |_| | |_) | |_| || |  
# |_| |_|\___/|_| |_|\___|\__, |____/ \___/ |_|  
#                         |___/                  
# Run me first!!!! I make sure everything is installed correctly.
# 
#

# TODO: PUT WEBSERVER IN CONTAINER ASAP

# setup part 1: install dependecies and prepare directories
mkdir -p gpt4all/models
mkdir output

# validate basic dependencies
if [[ "$OSTYPE" == "darwin"* ]]; then
    brew update && brew install wget git python@3.10 cmake protobuf rust git-lfs
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if [[ $(uname -n) == "fedora" ]]; then
        dnf install wget git python3 git-lfs
    else
        apt-get install -y wget git python3 git-lfs
    fi
fi
# TODO: make this run on arch

# create venv and setup
python3 -m venv .venv
source .venv/bin/activate


# install gpt4all & stable diffusion webui-api
pip install --upgrade pip
pip install -r requirements.txt
git lfs install

# install vicuna model for gpt4all
wget https://gpt4all.io/models/ggml-nous-gpt4-vicuna-13b.bin  -O ./gpt4all/modelsggml-nous-gpt4-vicuna-13b.bin

# install autogpt4all
git clone -b stable-copy https://github.com/mussar0x4D5352/autogpt4all.git && cd autogpt4all && chmod +x autogtp4all.sh && ./autogtp4all.sh && 
cd ../

# install stable-diffusion-webui and dependencies

git clone https://github.com/AUTOMATIC1111/stable-diffusion-webui 

# safety check for mac to ensure compatibility, linux doesn't need this
# TODO: verify that this is still needed
# TODO: set up a fork for this repo so we can make sure it's always compatible

if [[ "$OSTYPE" == "darwin"* ]]; then
    cd stable-diffusion-webui && git checkout dev && git pull 
fi

# install diffusion model of choice, change model number for diff purposes or if size constraints are needed.

# model options (full size is selected, remove the ? and everything after it for the standard sizes):
# https://civitai.com/api/download/models/86437?type=Model&format=SafeTensor&size=full&fp=fp16 - Absolute Reality, current default
# https://civitai.com/api/download/models/29460?type=Model&format=PickleTensor&size=full&fp=fp16 - Realisitic Vision, use as backup


cd ./models/Stable-diffusion && wget 'https://civitai.com/api/download/models/86437?type=Model&format=SafeTensor&size=full&fp=fp16' --content-disposition && cd ../../

# install textual inversions 

cd ./embeddings && wget https://civitai.com/api/download/models/77169 --content-disposition && wget https://civitai.com/api/download/models/77173 --content-disposition && cd ../

# install extensions 

cd ./extensions && git clone https://github.com/Bing-su/adetailer.git && cd ../

# install extension models

cd ./models && git clone https://huggingface.co/Bingsu/adetailer && cd ../

# launch webui in background mode with no webserver

./webui.sh --nowebui # --use-cpu # uncomment if you're not able to use your GPU
# TODO: figure out how to get this to launch in the background
# TODO: once that's implemented, do the same for the LocalAI script

# from here, open a new terminal window and execute run.sh COUNT IP, where COUNT is how many people you want to generate and IP is the server you're setting up your hive on.