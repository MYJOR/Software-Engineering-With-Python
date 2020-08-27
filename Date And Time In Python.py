# time function
import time
import datetime
from datetime import tzinfo



mytime=time.time()
print(mytime)

#time in seconds format

myctime=time.ctime(mytime)
print(myctime)

#formating time

formatime=time.strftime("%d-%m-%y.%H.%M.%S")
print(formatime)
'''time delta function '''
t1=datetime.timedelta(40)
t2=datetime.timedelta(80)
f=t2-t1
print(f)
'''doesn't work properly '''
timeformatted=datetime.datetime.now(tzinfo.timezone("Asia/Karachi"))
print(timeformatted)

