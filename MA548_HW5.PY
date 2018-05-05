import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib import style
from random import randint  
style.use('ggplot')

def q1(l,T):
	t = 0
	I = 0
	S = [0]
	B = [0]
	Bus = 0
	while t <= T:
		Bus += randint(20,40)
		U = np.random.uniform(0,1)
		t = t - np.log(U)/l
		S.append(t)
		B.append(Bus)
	plt.plot(S,B, drawstyle='steps-post',color = 'blue')
	plt.xlabel('times')  
	plt.ylabel('numbers')
	plt.xlim(0, 2)  
	plt.show()

	
def q2A(n, T):
	count = []
	for i in range (1,n):
		t = 0
		I = 0
		while t <= T:
			U = np.random.uniform(0,1)
			l = 1 + 0.6 * math.sin(t)
			t = t - np.log(U)/l
			I += 1
		count.append(I)
	return np.mean(count), np.var(count)

def q2B(n, T):
	count = []
	lmax = 1.6
	for i in range (1,n):
		t = 0
		I = 0
		while t <= T:
			U1 = np.random.uniform(0,1)
			l = 1 + 0.6 * math.sin(t)
			t = t - np.log(U1)/lmax
			pt = l/lmax
			if np.random.uniform(0,1) <= pt:
				I += 1
		count.append(I)
	return np.mean(count), np.var(count)

def true(t):
	return t - 0.6 * np.cos(t)

def plot_NA(n,rge):
	T = [0]
	S1 = [0]
	S2 = [0]
	SA = [0]
	i = 0
	while i <= n:
		mean = q2A(100,i)[0]
		sample_std = q2A(100,i)[1]/100
		S1.append(mean+1.96*np.sqrt(sample_std))
		S2.append(mean-1.96*np.sqrt(sample_std))
		SA.append(mean)
		T.append(i)
		i += rge
	plt.plot(T,S1)
	plt.plot(T,S2)
	plt.plot(T,SA)
	plt.plot(T,true(T))
	plt.xlabel('Times t')  
	plt.ylabel('E[N]')
	plt.xlim(0, 20) 
	plt.legend(['Up Level','Down Level','Naive Algorithm','Real Line']) 
	plt.fill_between(T,S2,S1,S1>S2,color='yellow',alpha=0.25)
	plt.show()

def plot_NHPP(n,rge):
	T = [0]
	S1 = [0]
	S2 = [0]
	SA = [0]
	i = 0
	while i <= n:
		mean = q2B(100,i)[0]
		sample_std = q2B(100,i)[1]/100
		S1.append(mean+1.96*np.sqrt(sample_std))
		S2.append(mean-1.96*np.sqrt(sample_std))
		SA.append(mean)
		T.append(i)
		i += rge
	plt.plot(T,S1)
	plt.plot(T,S2)
	plt.plot(T,SA)
	plt.plot(T,true(T))
	plt.xlabel('Times t')  
	plt.ylabel('E[N]')
	plt.xlim(0, 20) 
	plt.legend(['Up Level','Down Level','NHPP Algorithm','Real Line']) 
	plt.fill_between(T,S2,S1,S1>S2,color='yellow',alpha=0.25)
	plt.show()


def q3(n):
	j = 0
	x1, x2, x3 = 0, 0, 0
	S = 0
	P = np.array(([1/2 , 1/3 , 1/6],[0, 1/3, 2/3],[1/2, 0, 1/2]))
	for i in range (1,n):
		U = np.random.uniform(0,1)
		if U <= P[j][0]:
			j = 0
			x1 += 1
			S = S + 0
		elif U <= P[j][1]+P[j][0]:
			j = 1
			x2 += 1
			S = S + 1
		else :
			j = 2 
			x3 += 1
			S = S + 2
	print("\n[Question 3A:] \n")
	print(x1/n, x2/n, x3/n)
	print("\n[Question 3B:] \n")
	print(S/n)


q1(5,2)
print("\n[Question 2A(naive algorithm):] \n")
print("n=100 (mean,variance):", q2A(100,20))
plot_NA(20,0.5)
plot_NHPP(20,0.5)
print("\n[Question 2B(NHPP)] \n")
print("n=100 (mean,variance):", q2B(100,20))
q3(1000)

'''T = [0]
S1 = [0]
S2 = [0]
i = 10
while i:
	S1.append(q2A(100,i)[0]+1.96*np.sqrt(q2A(100,i)[1]))
	S2.append(q2A(100,i)[0]-1.96*np.sqrt(q2A(100,i)[1]))
	T.append(i)
	i -= 0.5
plt.plot(T,S1,'g-',drawstyle='steps-post',color = 'blue')
plt.plot(T,S2,'b-',drawstyle='steps-post',color = 'blue')
plt.xlabel('times')  
plt.ylabel('E[N]')
plt.xlim(0, 10)  
plt.fill_between(T,S2,S1,S1>S2,color='yellow',alpha=0.25)
plt.show()
'''