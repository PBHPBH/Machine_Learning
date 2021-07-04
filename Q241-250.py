import time
import datetime


day = datetime.datetime.now()
print(day)

now = datetime.datetime.now()
print(now, type(now))

for day in range(5, 0, -1):
    delta = datetime.timedelta(days=day)
    date = now - delta
    print(date)

now = datetime.datetime.now()
print(now.strftime("%H:%M:%S"))

day = "2020-05-04"
ret = datetime.datetime.strptime(day, "%Y-%m-%d")
print(ret, type(ret))

#while True:
 #   now = datetime.datetime.now()
  # print(now)
   # time.sleep(1)

#import A : A모듈을 import하라
#from B import A : A모듈로부터 B함수를 가져오라는 의미
#from A import * : 모둘내의 모든것을 가져옴

import os
ret = os.getcwd()
print(ret, type(ret))

#os.rename("C:/Users/gjsdl/Desktop/before.txt", "C:/Users/gjsdl/Desktop/after.txt")


import numpy
for i in numpy.arange(0, 5, 0.1):
    print(i)