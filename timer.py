import time
import os

while True:
    print(time.strftime('%Y-%m-%d %h:%M:%S',time.localtime(time.time())))
    os.system('cls')
    time.sleep(1)
