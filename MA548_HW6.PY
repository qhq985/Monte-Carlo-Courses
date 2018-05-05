import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import stats
from matplotlib import style 
from random import gauss
import matplotlib.pyplot as plt



def q1(lmt = 10, miu = 2, fie = 3, T = 100000):
	t = 0
	X = 0
	C = [0]		#long-run average number of customers in the shop
	B = 0		#long-run proportion of time the barber is busy
	F = 0		#long-run proportion of time the shop is full
	L = [0]		#long-run average number of customers waiting in line
	P = np.array(([0 , 1 , 0, 0],[miu/(miu+lmt), 0, lmt/(miu+lmt), 0],[0, (fie+miu)/(fie+miu+lmt), 0, lmt/(miu+lmt+fie)], [0, 0, 1, 0]))
	f = [lmt, lmt+miu, lmt+miu+fie, miu+2*fie]
	while t <= T:
		U = np.random.uniform(0,1)
		V = np.random.uniform(0,1)
		if V <= P[X][0]:
			X = 0
		elif V <= P[X][0]+P[X][1]:
			X = 1
		elif V <= P[X][0]+P[X][1] + P[X][2]:
			X = 2
		else:
			X = 3
		t_gap = - np.log(U)/f[X]
		t = t + t_gap
		C.append(X*t_gap)
		if X > 0:
			B += t_gap
		if X == 3:
			F += t_gap
		L.append(max(t_gap*(X - 1), 0))
	print('',np.sum(C)/T,'\n', B/T, '\n',F/T, '\n',np.sum(L)/T)

# Professor's formula
def Q2_BSprice(exper_time, S0, K):
		a = (np.log(K/S0)+exper_time/2-0.2*exper_time)/np.sqrt(exper_time)
		return a, stats.norm.cdf(-a, 0, 1), K*stats.norm.cdf(-a, 0 ,1)*np.exp(-0.2*exper_time), S0*stats.norm.cdf(np.sqrt(exper_time)-a, 0, 1) - K*stats.norm.cdf(-a, 0 ,1)*np.exp(-0.2*exper_time)

#Black and Scholes
def d1(S0, K, r, sigma, T):
    return (np.log(S0/K) + (r + sigma**2 / 2) * T)/(sigma * np.sqrt(T))
 
def d2(S0, K, r, sigma, T):
    return (np.log(S0 / K) + (r - sigma**2 / 2) * T) / (sigma * np.sqrt(T))
 
def BlackScholes(type,S0, K, r, sigma, T):
    if type=="C":
    	return S0 * stats.norm.cdf(d1(S0, K, r, sigma, T)) - K * np.exp(-r * T) * stats.norm.cdf(d2(S0, K, r, sigma, T))
    else:
    	return K * np.exp(-r * T) * stats.norm.cdf(-d2(S0, K, r, sigma, T)) - S0 * stats.norm.cdf(-d1(S0, K, r, sigma, T))
def Simulate_European_option(type, S0, K, r, sigma, T, N):
	Total_C = 0
	if type == 'C':
		for i in range (N):
			St = S0 * np.exp((r-sigma**2/2)*T + sigma*np.sqrt(T)*np.random.normal(0,1))
			C = np.exp(-r*T)*(max(St-K,0))
			Total_C += C

		return Total_C/N

	else:
		for i in range (N):
			St = S0 * np.exp((r-sigma**2/2)*T + sigma*np.sqrt(T)*np.random.normal(0,1))
			C = np.exp(-r*T)*(max(K-St,0))
			Total_C += C
		return Total_C/N

def Simulate_Asian_option(S0, K1, K2, K3, r, sigma, T, N, delta_time):
	Total_C1 = 0
	Total_C2 = 0
	Total_C3 = 0
	t = np.int(T/delta_time)
	for i in range(N):
		Sj = S0
		Total_Sj = S0
		for j in range(t):
			Sj = Sj * np.exp((r-sigma**2/2)*delta_time+sigma*np.sqrt(delta_time)*np.random.normal(0,1))
			Total_Sj += Sj
		C1 = np.exp(-r*T)*max(Total_Sj/t - K1, 0)
		C2 = np.exp(-r*T)*max(Total_Sj/t - K2, 0)
		C3 = np.exp(-r*T)*max(Total_Sj/t - K3, 0)
		Total_C1 += C1
		Total_C2 += C2
		Total_C3 += C3
	return Total_C1/N, Total_C2/N, Total_C3/N

def Simulate_Lookback_option(S0, r, sigma, T, N, delta_time):
	Total_C = 0
	t = np.int(T/delta_time)
	for i in range(N):
		Sj = S0
		Sj_next = S0
		Sj_down = S0
		for j in range (t):
			Sj_next = Sj_next * np.exp((r-sigma**2/2)*delta_time+sigma*np.sqrt(delta_time)*np.random.normal(0,1))
			if Sj_next <= Sj_down: 
				Sj_down = Sj_next
		C = np.exp(-r*T)*max(Sj_next - Sj_down, 0)
		Total_C += C
	return Total_C/N

def CoC(T1, T2, K1, K2, S, r, sigma, N):
	miu = r - sigma**2/2
	C0 = 0
	for i in range(N):
		St = S * np.exp(miu*T2+sigma*np.sqrt(T2)*np.random.normal(0,1))
		C = max(St - K2 - K1 * np.exp(r * (T2 - T1)), 0) * np.exp(-r * T2)
		C0 += C
	return C0/N

def JDP(S0, l, a, b2, r, sigma, T, delta_time):
	t = np.int(T/delta_time)
	miu = r - ( np.exp( a * 1 + b2/2)- 1) * l
	X = np.log(S0)
	SS=[S0]

	for i in range(t):
		Z = gauss(0,1)
		n = np.random.poisson(l*delta_time)
		j = 0
		M = 0
		if n == 0:
			M = 0
		else:
			for j in range(n):
				M += gauss(a, np.sqrt(b2))
		X = X + (miu - sigma**2/2)*delta_time+sigma*Z*np.sqrt(delta_time) +M
		S = np.exp(X)
		SS.append(S)
	C = np.exp(-a*T)*max(SS[-1]-100, 0)
	return SS,SS[-1], C, miu


print("\n[Question 1A(Barber Shop)] \n")
q1()
print("\n[Question 2A(BS Option Price)] \n")
print('K = 100, C =', BlackScholes('C', 100, 100, 0.2, 1, 4))
# T = 4 is really a long time 
print('K = 120, C =',BlackScholes('C', 100, 120, 0.2, 1, 4))
print('K = 80,  C =',BlackScholes('C', 100, 80, 0.2, 1, 4))

print("\n[Question 2B(Simulate European Option Price)] \n")
print('K = 100, C =', Simulate_European_option('C', 100, 100, 0.2, 1, 4, 10000))
print('K = 120, C =', Simulate_European_option('C', 100, 120, 0.2, 1, 4, 10000))
print('K = 80,  C =', Simulate_European_option('C', 100, 80, 0.2, 1, 4, 10000))

print("\n[Question 2C(Simulate Aisan Option Price)] \n")
print('K1 = 100, K2 = 120, K3 = 80, C =', Simulate_Asian_option(100, 100, 120, 80, 0.2, 1, 4, 10000, 0.01))

print("\n[Question 2D(Simulate Lookback Option Price)] \n")
print('C =', Simulate_Lookback_option(100, 0.2, 1, 4, 10000, 0.01))

# print("\n[Question 3(Simulate European Call on a call(CoC))] \n")
# print('C =', CoC(2, 4, 80, 120, 100, 0.2, 1, 10000))

# print("\n[Question 4(Option pricing under JDP)] \n")
# print('Question 4A: miu = r - ( np.exp( a * 1 + b2/2)- 1) * l\n')

# # miu = r - ( np.exp( a * 1 - b2/2)- 1) * l
# countJDP = 0
# print('Question 4B\n')
# for i in range(10000):
# 	countJDP += JDP(100, 1, 0, 1/2, 0.2, 1, 4, 0.01)[2]
# print(countJDP/10000)
# for i in range(10):
# 	plt.plot(JDP(100, 1, 0, 1/2, 0.2, 1, 4, 0.01)[0])
# 	plt.xlabel('times')  
# 	plt.ylabel('numbers')
# 	plt.xlim(0, 400) 



# plt.show()
	
