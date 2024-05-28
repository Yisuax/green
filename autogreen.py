# autogreen.py
from datetime import datetime

with open('green.txt', 'a') as file:
    file.write(f"{datetime.now()}\n")
z
