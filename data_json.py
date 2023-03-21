import os
import json

FULL_PATH = os.path.dirname(os.path.abspath(__file__))
path_auth = FULL_PATH+'\\files\\for_json\\auth_data.json'
open_auth = open(path_auth)
data_auth = json.load(open_auth)

correct_username = data_auth['correct_username']
correct_password = data_auth['correct_password']
incorrect_username = data_auth['incorrect_username']
incorrect_password = data_auth['incorrect_password']
locked_out_username = data_auth['locked_out_username']