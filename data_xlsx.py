import os
import pandas as pd
# import openpyxl

FULL_PATH = os.path.dirname(os.path.abspath(__file__))
path_errors = FULL_PATH+'\\files\\for_xlsx\\errors.xlsx'
open_errors = pd.ExcelFile(path_errors)
data_errors = open_errors.parse('auth_er')

locked_out = data_errors['auth_errors'][0]
not_match = data_errors['auth_errors'][1]
empty_login = data_errors['auth_errors'][2]
empty_password = data_errors['auth_errors'][3]

