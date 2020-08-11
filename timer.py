import time

while True:
    print(time.strftime('%Y-%m-%d %h:%M:%S',time.localtime(time.time())))
    time.sleep(1)