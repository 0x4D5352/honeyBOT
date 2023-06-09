# add users to the current linux system
# Usage: python add_users.py
# NOTE - this code was writting with the assistance of GitHub Copilot.
import os
import json
from secrets import randbelow
import sys
from time import sleep
import fabric


# set the output directory
OUTPUT_DIRECTORY = os.path.join(os.getcwd(), "output")
# grab the value of the id_rsa file stored in ~/.ssh and store it in a variable
SSH_KEY = os.path.join(os.path.expanduser("~"), ".ssh/id_rsa")

# go through the output folder and create a dictionary based on the contents of logins.json
def create_dict(login_json):
    # open the logins.json file
    with open(login_json, 'r') as f:
        fix = json.loads(json.dumps(f.read())) # i messed something up and this is a quick fix
        # load the contents of the file into a dictionary
        data = json.loads(fix)
        # create a dictionary to store the contents for the logins
        logins = {}
        # add the username as the key and randomly select the password for the value
        logins['Username'] = data['Username'] 
        logins['Password'] = data[['Password1', 'Password2', 'Password3'][randbelow(3)]]
        # return the dictionary
        return logins


# go through the output directory and create a dictionary based on the contents of logins.json in each folder
def main():
    # take the argument from the command line and place it in the variable server
    server = sys.argv[1]
    # if there is no server, warn the user and exit the program
    if not server:
        print("Please provide a server to connect to.")
        exit()
    # using fabric, ssh into the server as root using your SSH key
    print("Connecting to the server...")
    user = fabric.Connection(server, user="root", connect_kwargs={"key_filename": SSH_KEY}).run("echo $USER")
    # if $USER is root, continue
    if user.stdout == "root\n":
        # show the end of the /etc/passwd file
        fabric.Connection(server, user="root", connect_kwargs={"key_filename": SSH_KEY}).run("tail /etc/passwd")
        print("\n\n\nAdding users to the system...")
        # go through the output directory
        for person in os.listdir(OUTPUT_DIRECTORY):
            # if the first character of the folder name is not a period
            if person[0] != '.':
                # create a dictionary based on the contents of logins.json in each folder
                logins = create_dict(f"{OUTPUT_DIRECTORY}/{person}/logins.json")
                # add the users to the system
                print(f"Adding {logins['Username']} to the system...")
                fabric.Connection(server, user="root", connect_kwargs={"key_filename": SSH_KEY}).run(f"useradd -m -p {logins['Password']} {logins['Username']} &")
        # verify that the users were added to the system
        fabric.Connection(server, user="root", connect_kwargs={"key_filename": SSH_KEY}).run("tail /etc/passwd")
            
# run the main function
if __name__ == "__main__":
    main()
    
