#program for showing the real time

from datetime import datetime
import time
import random
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
right_this_minute = datetime.today().minute
write_this_hour = datetime.today().hour
print('Hour:',write_this_hour)
for t in range(5):
    if right_this_minute in odds:
        print("This minute seens a little odd")
else:
    print("Not an odd minute:")
  wait_time = random.randint(1, 60)
  time.sleep(wait_time)

