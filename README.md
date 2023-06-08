# 🍯🤖 honeyBOT 🤖🍯

*Fake People, Solving Real Security Problems*

honeyBOT leverages the power of multiple FOSS Generative AI Models to construct realistic people with realistic backstories, realistic photos, and most importantly - realistic bad passwords. Using FOSS tools allows honeyBOT to generate an unlimited number of inferences hosted locally on your machine. No rate limits, no API fees, no censorship, and (after your first runthrough) entirely offline. Whether you need a single person for a spear phishing or BEC campaign, or an entire fictional organization that exists on a bait server in your DMZ, honeyBOT can provide!

In this current implementation, honeyBOT will generate backgrounds, photos, and passwords for a specified number of people and add them to the specified Linux server. Future versions will allow for more customization, including the ability to generate people with specific backgrounds, photos, and passwords.

## 🐝 How to Use 🐝

### Step 1 (Mac/Linux).

Mac users: If you do not already have [Homebrew](https://brew.sh) installed, do so before running.
Windows setup is currently in development and will be released ASAP.

Only necessary for initial installation. See note for subsequent runs. Run the following text in your terminal:
```bash
git clone https://github.com/mussar0x4D5352/honeyBOT.git && cd ./honeyBOT && chmod +x *.sh && ./setup.sh
```
>🚨 NOTE: If you close the terminal session or shut down your computer, you will need to relaunch the stable diffusion webserver before continuing onto step 2:
```bash
cd stable-diffusion-webui && ./webui.sh
```


### Step 2.

Open a new terminal window and run `./run.sh COUNT SERVER`, replacing `COUNT` with the number of people you wish to generate and `SERVER` with the user and linux server you wish to add them to. For example, to generate five people on server 192.168.123.111:

```bash
./run.sh 5 "root@192.168.123.111"
```
>🚨 NOTE: In the current implementation, it is assumed that you have added your RSA key to the root account's authorized keys on the target server. This is to avoid requiring the user to monitor the account creation process.

## ⚠️ Warnings ⚠️

* honeyBOT has primarily been tested on macOS with an M1 ARM processor. It should work on Intel macs and most Linux distributions, provided you have a PyTorch compatiable graphics card.
* Image generation models are taken from Civitai, which occasionally suffers from connection issues which can cause the setup script to fail. If this happens, just reinitialize the repo and rerun.
* As with all generative models, hallucinations can still appear. Great care has been taken to minimize these issues, but always double check your results for errors and keep in mind they can be subtle!
* Launching the webserver tends to take total control of the terminal window and running it with & to send it into the background is currently an inconsistent solution, so two terminal sessions are recommended.

## 🛠️ Tools/Resources used 🛠️

* [GPT4ALL](https://gpt4all.io/index.html)
* [Stable Diffusion Web UI Server](https://github.com/AUTOMATIC1111/stable-diffusion-webui)
* [SD Webui API](https://github.com/mix1009/sdwebuiapi)
* [Civitai](https://civitai.com/) (warning: NSFW content)
* [Hugging Face](https://huggingface.co/)

## 🚗 Roadmap 🚗

* ~honeyBOT.generator Part 1 - First Release/MVP~ Done!
* honeyBOT.generator Refactor - Major rewrites for improvements, including containerization, are top priority.
* honeyBOT Expensive Mode - Don't have time, but have the money? Here's a version with the OpenAI API!
* honeyBOT.generator Part 2 - "Intelligent Design" mode, allowing you to customize different steps of the creation process.
* honeyBOT.buzz - use voice synthesis to create a soundboard and other interactive voice messages for the honeyBOT.
* honeyBOT.drone - Use AutoGPT4All to implement AutoGPT interaction for clicking dangerous email links, posting on social media, etc.
* honeyBOT.hive - bait server that allows drones to act autonomously in an isolated network environment, tempting attackers with their sweet smelling bad OpSec honey.
* honeyBOT.more - Just wait and see!
