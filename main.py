import datetime
import os
stop = False
while stop == False:
    rn = str(datetime.datetime.now().time())
    print(rn)
    if rn > '17:00:0.000000':
        stop = True
        print("OK")
        break
        #os.system("ring.mp3")



        
