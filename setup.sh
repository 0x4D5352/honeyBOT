#!/bin/bash               
# Run me first!!!! I make sure everything is installed correctly.
# (I'll fill the rest of this in later) 
#
#
#
#
#
#
#
tail -n 6 .honeybot.txt

# TODO: PUT everything in containers

# setup part 1: install dependecies and prepare directories
echo "Setting up honeyBOT environment..."
# check if gpt4all directory exists, if not, create it
if [ ! -d "gpt4all" ]; then
    mkdir -p gpt4all/models 
fi
if [ ! -d "output" ]; then 
    mkdir output
fi

echo "Installing dependencies..."

# validate basic dependencies
if [[ "$OSTYPE" == "darwin"* ]]; then
    brew update && brew install wget git python@3.10 cmake protobuf rust git-lfs docker docker-compose
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    if [[ $(uname -n) == "fedora" ]]; then
        dnf install wget git python3 git-lfs docker docker-compose
    else
        apt-get install -y wget git python3 git-lfs docker docker-compose
    fi
fi
# TODO: make this run on arch

# TODO: fix this
# validate docker install
#if ! [ -x "$(command -v docker)" ]; then
#    echo "Docker is not installed. Please install docker and run this script again."
#    exit 1
#elif [ $(docker ps) == "Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?" ]; then
#    echo "Docker is not running. Please start docker and run this script again."
#    exit 1
#fi


# check if $OPENAI_API_KEY is set
if [ -z ${OPENAI_API_KEY+x} ]; then
    echo "You need an OpenAI API key to run Auto-GPT."
    echo "If you do not already have one, you can get one here: https://platform.openai.com/account/api-keys"
    echo "Once you have your API key, set it as an environment variable called OPENAI_API_KEY, reload your shell and run this script again."
    exit 1
fi

# TODO: figure out how to check docker-compose version and update if older than 1.29.2

echo "Creating python environment..."

# create venv and setup
python3 -m venv .venv
source .venv/bin/activate

echo "Installing python dependencies..."

# install gpt4all & stable diffusion webui-api
pip install --upgrade pip
pip install -r requirements.txt
git lfs install

# install vicuna model for gpt4all
# TODO: figure out why this doesn't get loaded into gpt4all when it runs in generate_person
# wget https://gpt4all.io/models/ggml-nous-gpt4-vicuna-13b.bin  -O ./gpt4all/modelsggml-nous-gpt4-vicuna-13b.bin

# install autogpt4all
# git clone -b stable-copy https://github.com/mussar0x4D5352/autogpt4all.git && cd autogpt4all && chmod +x autogtp4all.sh && ./autogtp4all.sh && 
# cd ../

# install Auto-GPT repo

echo "Installing Auto-GPT..."

git clone -b stable https://github.com/Significant-Gravitas/Auto-GPT.git && cd ./Auto-GPT 

# set up Auto-GPT environment with OpenAI API key

cp .env.template .env

sed -i '' -e "s/your-openai-api-key/$OPENAI_API_KEY/g" .env

# enable local command execution (necessary for SSH)

sed -i '' -e "s/# EXECUTE_LOCAL_COMMANDS=False/EXECUTE_LOCAL_COMMANDS=True/g" .env

# curl -o ./plugins/Auto-GPT-SystemInfo.zip https://github.com/hdkiller/Auto-GPT-SystemInfo/archive/refs/heads/master.zip 

docker-compose build auto-gpt

cd ../

# install stable-diffusion-webui and dependencies

echo "Installing stable-diffusion-webui..."
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

echo "Installing Stable Diffusion model and dependencies..."

cd ./models/Stable-diffusion && wget 'https://civitai.com/api/download/models/86437?type=Model&format=SafeTensor&size=full&fp=fp16' --content-disposition && cd ../../

# install textual inversions 

cd ./embeddings && wget https://civitai.com/api/download/models/77169 --content-disposition && wget https://civitai.com/api/download/models/77173 --content-disposition && cd ../

# install extensions 

cd ./extensions && git clone https://github.com/Bing-su/adetailer.git && cd ../

# install extension models

cd ./models && git clone https://huggingface.co/Bingsu/adetailer && cd ../

# launch webui in background mode with no webserver

echo "Launching Stable Diffusion WebUI..."

./webui.sh --nowebui # --use-cpu # uncomment if you're not able to use your GPU
# TODO: figure out how to get this to launch in the background
# TODO: once that's implemented, do the same for the LocalAI script

# from here, open a new terminal window and execute run.sh COUNT IP, where COUNT is how many people you want to generate and IP is the server you're setting up your hive on.
