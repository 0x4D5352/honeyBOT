# add users to the current linux system
# Usage: python add_users.py
# NOTE - this code was writting with the assistance of GitHub Copilot.
import os
import json
from secrets import randbelow
import sys

# set the output directory
OUTPUT_DIRECTORY = os.path.join(os.getcwd(), "output")

# go through the output folder and create a dictionary based on the contents of logins.json
def create_dict(login_json):
    # open the logins.json file
    with open(login_json, 'r') as f:
        # load the contents of the file into a dictionary
        data = json.load(f)
        # create a dictionary to store the contents of the logins.json file
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
    # ssh into the server using your SSH key
    os.system(f"ssh -i ~/.ssh/id_rsa {server}")
    # switch to root user
    os.system("sudo su")
    # go through the output directory
    for person in os.listdir(OUTPUT_DIRECTORY):
        # if the first character of the folder name is not a period
        if person[0] != '.':
            # create a dictionary based on the contents of logins.json in each folder
            logins = create_dict(f"{OUTPUT_DIRECTORY}/{person}/logins.json")
            # add the users to the system
            os.system(f"useradd -m -p {logins['Username']} {logins['Password']} &")
    # verify that the users were added to the system
    os.system("cat /etc/passwd")
    # exit the server
    os.system("exit")
            
# run the main function
if __name__ == "__main__":
    main()
    