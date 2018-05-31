import  read
import pandas as pd
import collections as cl
data1 = read.load_data()
longstr = ''
for index,each in data1.iterrows():
    longstr = longstr + ' ' + str(each['headline'])
longstr_spl = longstr.split(' ')
longstr_spl_lower = []
for each in longstr_spl:
    longstr_spl_lower.append(each.lower())
count_str = cl.Counter(longstr_spl_lower)
print(count_str.most_common(100))