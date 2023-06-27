# 🍯🤖 honeyBOT 🤖🍯

*Fake People, Solving Real Security Problems*

honeyBOT leverages the power of multiple FOSS Generative AI Models to construct realistic people with realistic backstories, realistic photos, and most importantly - realistic bad passwords. Using FOSS tools allows honeyBOT to generate an unlimited number of inferences hosted locally on your machine. No rate limits, no API fees, no censorship, and (after your first runthrough) entirely offline. Whether you need a single person for a spear phishing or BEC campaign, or an entire fictional organization that exists on a bait server in your DMZ, honeyBOT can provide!

The final implementation of honeyBOT will be comprised of three main components - the queen, the drones, and the hive:
* honeyBOT.queen - The primary engine for honeyBOT, which leverages GPT4ALL and Stable Diffusion to generate drones to populate your hive. 
* honeyBOT.drone - A less-than-secure user, using Auto-GPT to perform tasks like clicking links in emails and reusing the same memorable passwords on multiple websites. 
* honeyBOT.hive - A virtual machine, virtual network, or web API that your drones either connect to or run on in order to perform their tasks - drawing attention away from the rest of your organization. 

In its current form, honeyBOT will generate backgrounds, photos, and passwords for an arbitrary number of people, generates sample posts for social media, and adds them to a Linux server you have control over. Future versions will allow for more customization, including the ability to generate people with specific backgrounds, photos, and passwords. 

>🚨 NOTE: If you have an OpenAI API key and the inclination to spend a bit of money, you can test out basic agent usage by checking out the dev branch or uncommenting the relevant lines of text in `setup.sh` and `run.sh`. 
>In testing, using GPT-4 to perform a basic system administration task took about $2.00 USD and 22 minutes of realtime, but prompt engineering tests and 3.5/4 comparison tests cost an additional $5.25 USD and a few hours of realtime.
>Be sure to set a usage limit in both Auto-GPT and on OpenAI's billing page before doing so!

## 🐝 How to Use 🐝

### Prerequisites:
Mac users: If you do not already have [Homebrew](https://brew.sh) installed, do so before running.
Windows setup is currently in development and will be released ASAP.

For `run.sh` to work, you need to have access to a linux server you can connect to via SSH. It's recommended that you set up a VM on your local network or a VLAN, especially for interacting with Auto-GPT. See the note in step 2 for more details.

### Step 1 (Mac/Linux).

Only necessary for initial installation. See note for subsequent runs. Run the following text in your terminal:
```bash
git clone https://github.com/mussar0x4D5352/honeyBOT.git && cd ./honeyBOT && chmod +x *.sh && ./setup.sh
```
>🚨 NOTE: If you close the terminal session or shut down your computer, you will need to relaunch the stable diffusion webserver before continuing onto step 2:
```bash
# assuming you're already in honeyBOT/
cd ./stable-diffusion-webui && ./webui.sh
```


### Step 2.

Open a new terminal window, navigate to the demo directory, and run `./run.sh COUNT SERVER`, replacing `COUNT` with the number of people you wish to generate and `SERVER` with the user and linux server you wish to add them to. For example, to generate five people on server 192.168.123.111:

```bash
cd demo && ./run.sh 5 "root@192.168.123.111"
```
>🚨 NOTE: In the current implementation, it is assumed that you have added your RSA key to the root account's authorized keys on the target server. This is to avoid requiring the user to monitor the account creation process. Don't do this on a live server.

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
* [Auto-GPT](https://github.com/Significant-Gravitas/Auto-GPT)

## 🚗 Roadmap 🚗

* ~honeyBOT.generator Part 1 - First Release/MVP~ Done!
* honeyBOT.generator Refactor - Major rewrites for improvements, including containerization, are top priority.
* honeyBOT Expensive Mode - Don't have time, but have the money? Here's a version with the OpenAI API!
* honeyBOT.generator Part 2 - "Intelligent Design" mode, allowing you to customize different steps of the creation process.
* honeyBOT.buzz - use voice synthesis to create a soundboard and other interactive voice messages for the honeyBOT.
* honeyBOT.drone - Use AutoGPT4All to implement AutoGPT interaction for clicking dangerous email links, posting on social media, etc.
* honeyBOT.hive - bait server that allows drones to act autonomously in an isolated network environment, tempting attackers with their sweet smelling bad OpSec honey.
* honeyBOT.more - Just wait and see!
