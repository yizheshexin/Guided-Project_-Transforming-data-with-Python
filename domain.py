import  read
import pandas as pd
import collections as cl
data2 = read.load_data()
loopcount = 0
for name ,row in data2['url'].value_counts().items():
    loopcount += 1
    print('{}  {}:{}'.format(loopcount,name,row))
    if loopcount == 100:
        break
        