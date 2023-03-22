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

path_products = FULL_PATH+'\\files\\for_json\\products_data.json'
open_products = open(path_products)
data_products = json.load(open_products)

name_A_to_Z = data_products['name_A_to_Z']
name_products_up = data_products['name_products_up']

name_Z_to_A = data_products['name_Z_to_A']
name_products_down = name_products_up[::-1]

price_l_to_h = data_products['price_l_to_h']
price_products_up = data_products['price_products_up']

price_h_to_l = data_products['price_h_to_l']
price_products_down = price_products_up[::-1]
