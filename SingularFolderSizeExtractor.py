# -*- coding: utf-8 -*-

import os
import csv
import time

path = r'C:\Users\fugufugu\Downloads\2-tmp\Mugic.Movie.etc'
outpath = r'C:\Users\fugufugu\Downloads\books\text'
def gettime():
    now = time.time_ns()
    nowms = now/(10**6)
    return nowms
timestamp = []
stampdesc = []
timestamp.append(gettime())
stampdesc.append('initial')
def csvs (path,i):
    with open(path,'a',newline='') as csv1:
        sr = csv.writer(csv1)
        sr.writerow([i])
lists = os.listdir(path)
timestamp.append(gettime())
stampdesc.append('getdir')
tmp1 = path.split('\\')
for i in lists:
    o = os.path.isfile(f'{path}\{i}')
    if o == True:
        n = 0
        csvs(f'{outpath}\{tmp1[len(tmp1)-1]}.csv',os.path.getsize(f'{path}\{i}'))
timestamp.append(gettime())
stampdesc.append('finish')
print(timestamp[len(timestamp)-1]-timestamp[0])
