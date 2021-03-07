import string
import random
import clipboard
import eel
import re
import csv
from pathlib import Path
import gspread

eel.init('web')

scope = ['https://www.googlapis.com/feeds',
         'https://www.googlapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googlapis.com/auth/drive']

@eel.expose
def PassGen(accname,passlen):
    while True:
        s1 = string.ascii_lowercase
        s2 = string.ascii_uppercase
        s3 = string.digits
        s4 = string.punctuation
        s = []
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))
        global passcode 
        global acccname
        acccname = accname
        passcode = "".join(random.sample(s, passlen))
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,18}$"
        match_re = re.compile(reg)
        res = re.search(match_re, passcode)
        if res:
            result = 'Account :- ' + accname + '\nPassword\n' + passcode
            return result

@eel.expose
def sheetsave():
    gc = gspread.service_account(filename="error.json")
    sheet = gc.open("Python").sheet1
    sheet.append_row([acccname,passcode])

@eel.expose
def pycopy():
    clipboard.copy(passcode)


eel.start('index.html',size = (600,551)) #for edge browser use mode = 'edge'



