import json

# wrapper function for converting a json file to a dictionary
def json_to_dict(json_file):
    # open the json file
    with open(json_file, 'r') as f:
        # convert the json file to a dictionary
        data = json.loads(f)
        # return the dictionary
        return data
    
# wrapper function for converting a dictionary to a json file
def dict_to_json(dictionary, json_file):
    # open the json file
    with open(json_file, 'w') as f:
        # convert the dictionary to a json file
        json.dump(dictionary, f)
