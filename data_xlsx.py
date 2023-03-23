import os
import pandas as pd
# import openpyxl

FULL_PATH = os.path.dirname(os.path.abspath(__file__))
path_errors = FULL_PATH+'\\files\\for_xlsx\\errors.xlsx'
open_errors = pd.ExcelFile(path_errors)
auth_er = open_errors.parse('auth_er')
cart_er = open_errors.parse('cart_er')

locked_out = auth_er['auth_errors'][0]
not_match = auth_er['auth_errors'][1]
empty_login = auth_er['auth_errors'][2]
empty_password = auth_er['auth_errors'][3]

name_req = cart_er['cart_errors'][0]
l_name_req = cart_er['cart_errors'][1]
p_code_req = cart_er['cart_errors'][2]

