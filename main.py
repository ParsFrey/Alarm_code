import datetime
import os
stop = False
while stop == False:
    rn = str(datetime.datetime.now().time())
    print(rn)
    x = int(datetime.datetime.now().time() + '00:00:10.000000')
    if rn > x:
        stop = True
        print("OK")
        break
        #os.system("ring.mp3")


        