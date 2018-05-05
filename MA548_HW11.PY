import numpy as np
import csv
import pandas as pd 
import matplotlib.pyplot as plt
import math

data = pd.read_excel('arrivals.xls')



day = []
day2 = []



for i in range(12):
    inter = data[data <= (i+1)*10]
    inter = inter[data >= i*10]
    inter.fillna(0,inplace = True)
    inter[inter>0]=1
    day.append(inter.sum().mean()/10)

for i in range(24):
    inter = data[data <= (i+1)*5]
    inter = inter[data >= i*5]
    inter.fillna(0,inplace = True)
    inter[inter>0]=1
    day2.append(inter.sum().mean()/5)

def l(t):
    y = np.cos(2*math.pi*t/120)+1
    
    return y

t1 = np.arange(0,120,10)
t2 = np.arange(0,120,5)
plt.figure()
plt.plot(l(t1),color = 'red',linewidth=1.0, linestyle='--')
plt.plot(day)
plt.xlabel('Subintervals for 10 mintues')
plt.ylabel('Rate per minute')
plt.xlim((0,12))

plt.figure('Figure 2')
plt.plot(l(t2),color = 'red',linewidth=1.0, linestyle='--')
plt.plot(day2)
plt.xlabel('Subintervals for 5 mintues')
plt.ylabel('Rate per minute')
plt.xticks(np.arange(0, 26, 2.0))

plt.show();

 

