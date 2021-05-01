import requests
import random
import os
from time import sleep
code = random.randint(1111, 9999)
ID = input('Enter telegram ID : ')
sleep(1)
token = '' # here you put your bot token .
tele = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={ID}&text=your code is : {code}'
req = requests.get(tele).text
if '"ok":true,"result"' in req:
    print('Your code was sended !')
else:
    print('Error')
    exit()
sleep(1)
code_log = input('Enter Code : ')
sleep(1)
if code_log == f'{code}':
    print('Logged in ! ')
else:
    print('Error')
    exit()
