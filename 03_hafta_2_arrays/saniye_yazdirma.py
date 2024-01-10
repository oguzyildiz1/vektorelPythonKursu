import time
import datetime


while True:
    simdi = datetime.datetime.now()
    print(simdi.strftime("%H:%M:%S"))
    time.sleep(1)

