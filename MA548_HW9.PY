from random import randint  
import numpy as np
import math
from scipy import stats


def Q1A(N): 
	count = []
	C = []
	U = []
	for i in range(N):
		num = 0
		result = []
		while len(result)<11:
			dice1 = randint(1,6)
			dice2 = randint(1,6)
			sum = dice1 + dice2 
			if sum not in result:
				result.append(sum)
			num += 1
		UU = randint(1,6)
		U.append(UU)
		count.append(num)

	C_star = -np.cov(count,U, ddof =1)[0][1]/np.var(U, ddof = 1)
	for j in range(N):
		C.append(count[j]+C_star*(U[j]-3))

	m = np.mean(C)
	sigma = np.std(C, ddof = 1)

	return sigma**2, m - 1.96 * sigma/N**0.5, m + 1.96 * sigma/N**0.5

def Q2_BSprice(exper_time, S0, K):
		a = (np.log(K/S0)+exper_time/2-0.2*exper_time)/np.sqrt(exper_time)
		return S0*stats.norm.cdf(np.sqrt(exper_time)-a, 0, 1) - K*stats.norm.cdf(-a, 0 ,1)*np.exp(-0.2*exper_time)

def Simulate_European_option(type, S0, K, r, sigma, T, N):
	Total_C = []
	if type == 'C':
		for i in range (N):
			St = S0 * np.exp((r-sigma**2/2)*T + sigma*np.sqrt(T)*np.random.normal(0,1))
			C = np.exp(-r*T)*(max(St-K,0))
			Total_C.append(C)
		m = np.mean(Total_C)
		sigma = np.std(Total_C,ddof =1)
		return m - 1.96 * sigma/N**0.5, m + 1.96 * sigma/N**0.5

	else:
		for i in range (N):
			St = S0 * np.exp((r-sigma**2/2)*T + sigma*np.sqrt(T)*np.random.normal(0,1))
			C = np.exp(-r*T)*(max(K-St,0))
			Total_C.append(C)
		m = np.mean(Total_C)
		sigma = np.std(Total_C,ddof =1)
		return m - 1.96 * sigma/N**0.5, m + 1.96 * sigma/N**0.5

def Simulate_Asian_option(S0, K1, K2, K3, r, sigma, T, N, delta_time):
	Total_C1 = []
	Total_C2 = []
	Total_C3 = []
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
		Total_C1.append(C1)
		Total_C2.append(C2)
		Total_C3.append(C3)

	m1 = np.mean(Total_C1)
	sigma1 = np.std(Total_C1,ddof =1)
	m2 = np.mean(Total_C2)
	sigma2 = np.std(Total_C2,ddof =1)
	m3 = np.mean(Total_C3)
	sigma3 = np.std(Total_C3,ddof =1)
	return [m1 - 1.96 * sigma1/N**0.5, m1 + 1.96 * sigma1/N**0.5],[m2 - 1.96 * sigma2/N**0.5, m2 + 1.96 * sigma2/N**0.5],[m3 - 1.96 * sigma3/N**0.5, m3 + 1.96 * sigma3/N**0.5]

def Simulate_Lookback_option(S0, r, sigma, T, N, delta_time):
	Total_C = []
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
		Total_C.append(C)
	m = np.mean(Total_C)
	sigma = np.std(Total_C,ddof =1)
	return m - 1.96 * sigma/N**0.5, m + 1.96 * sigma/N**0.5

def Q1C(N):
	m = math.e
	sigma = np.sqrt(0.7658)
	return [m - 1.96 * sigma/N**0.5, m + 1.96 * sigma/N**0.5], 1.96 * sigma/N**0.5
	

def Q2A(N):
	X = np.exp(np.random.uniform(0,1,N)**2)
	m = np.mean(X)
	sigma = np.std(X, ddof = 1)
	return m - 2.33 * sigma/N**0.5, m + 2.33 * sigma/N**0.5

def Q2B(N):
	'''Antithetic variable estimator'''
	X = []
	for i in range(N):
		U = np.random.uniform(0,1)
		X.append((np.exp(U**2)+np.exp((1-U)**2))/2)
	m = np.mean(X)
	sigma = np.std(X, ddof = 1)
	return m - 2.33 * sigma/N**0.5, m + 2.33 * sigma/N**0.5

def Q2C(N):
	'''Control variate estimator using U as a control variable (first estimate C*)'''
	X = []
	UU = []
	C = []
	for i in range(N):
		U = np.random.uniform(0,1)
		X.append(np.exp(U**2))
		UU.append(U)

	C_star = -np.cov(X,UU, ddof =1)[0][1]/np.var(UU, ddof = 1)
	for i in range(N):
		C.append(X[i]+C_star*(UU[i]-1/2))
	m = np.mean(C)
	sigma = np.std(C, ddof = 1)
	return C_star, m - 2.33 * sigma/N**0.5, m + 2.33 * sigma/N**0.5

def Q2D(N):
	'''Combining the antithetic variable and control variate methods'''
	X = []
	U1 = []
	U2 = []
	W = []
	C = []
	CC = []
	for i in range(N):
		U = np.random.uniform(0,1)
		U1.append(U)
		U2.append(1-U)
		X.append(np.exp(U**2))
		W.append(np.exp((1-U)**2))
	#  I have question here, what is the smallest C*??????????
	a_star = 0.54
	C_star = (1-2*a_star)*np.cov(X,U1,ddof=1)[0][1]/np.var(U1,ddof=1)
	for i in range(N):
		C.append(a_star*X[i]+(1-a_star)*W[i]+C_star*(U1[i]-1/2))
	m = np.mean(C)
	sigma = np.std(C, ddof = 1)
	return a_star, C_star,m - 2.33 * sigma/N**0.5, m + 2.33 * sigma/N**0.5

def Q2E(N):
	'''Stratified sampling estimator by stratifying on U'''
	pass


def Q3A(N):
	'''Crude Monte-Carlo estimator X'''
	X = []
	for i in range(N):
		U1 = np.random.uniform(0,1)
		U2 = np.random.uniform(0,1)
		V1 = 2*U1-1
		V2 = 2*U2-1
		if V1**2 + V2**2 <= 1:
			X.append(1)
		else:
			X.append(0)
	return np.var(X, ddof =1)

def Q3B(N):
	'''Conditioning estimator on the variable V1'''
	# P[X|V1 = v] = P[V1^2 + V2^2 <= 1|V1 =v] = P[V2^2<1-v^2]
	#  = intergal(-sqrt(1-v^2),sqrt(1-v^2))of 1/2) = sqrt(1-v^2)
	X = []
	for i in range(N):
		U1 = np.random.uniform(0,1)
		V1 = 2*U1-1
		X.append(np.sqrt(1-V1**2))
	return np.var(X, ddof = 1)

def Q3C(N):
	'''Improved estimator of (b) using antithetic variables'''
	X = []
	for i in range(N):
		U = np.random.uniform(0,1)
		X.append((np.sqrt(1-U**2)+np.sqrt(1-(1-U)**2))/2)
	return np.var(X, ddof =1)

def Q3D(N):
	'''Improved estimator of (b) using (1) U1 and (2) U2
1 as control variates.'''
	X = []
	UU1 = []
	C1 = []
	UU2 = []
	C2 = []
	for i in range(N):
		U = np.random.uniform(0,1)
		X.append(np.sqrt(1-U**2))
		UU1.append(U)
		UU2.append(U**2)
	C_star1 = -np.cov(X,UU1, ddof =1)[0][1]/np.var(UU1, ddof = 1)
	C_star2 = -np.cov(X,UU2, ddof =1)[0][1]/np.var(UU2, ddof = 1)
	for i in range(N):
		C1.append(X[i]+C_star1*(UU1[i]-1/2))
		C2.append(X[i]+C_star2*(UU2[i]-1/3))
	return np.var(C1, ddof =1), np.var(C2, ddof =1)

print("[Question 1] \n")
print('(A) Use control variate or reduce by condition CI is', Q1A(10000))
print("\n[Question 2A(BS Option Price)] \n")
print('K = 100, C =', Q2_BSprice(4, 100, 100))
# T = 4 is really a long time 
print('K = 120, C =',Q2_BSprice(4, 100, 120))
print('K = 80,  C =',Q2_BSprice(4, 100, 80))

print("\n[Question 2B(Simulate European Option Price)] \n")
print('K = 100, C =', Simulate_European_option('C', 100, 100, 0.2, 1, 4, 100000))
print('K = 120, C =', Simulate_European_option('C', 100, 120, 0.2, 1, 4, 100000))
print('K = 80,  C =', Simulate_European_option('C', 100, 80, 0.2, 1, 4, 100000))

print("\n[Question 2C(Simulate Aisan Option Price)] \n")
print('K1 = 100, K2 = 120, K3 = 80, C =', Simulate_Asian_option(100, 100, 120, 80, 0.2, 1, 4, 100000, 0.01))

print("\n[Question 2D(Simulate Lookback Option Price)] \n")
print('C =', Simulate_Lookback_option(100, 0.2, 1, 4, 100000, 0.01))

print("[Question 1C] \n")
print('[Question 1(C) CI and error is', Q1C(2941857))

print("\n\n[Question 2] \n")
print('(A) Raw MC estimator CI is', Q2A(10000))
print('(B) Antithetic variable estimator CI is', Q2B(10000))
print('(C) Control variable estimator C_star and CI is', Q2C(10000))
print('(D) Antithetic & Control variate estimator a* and C* CI is', Q2D(10000))
print('(E) Stratffed sampling estimator CI is', Q2E(10000),'\n')


print("[Question 3] \n")
print('(A) Raw MC estimator variance is', Q3A(10000))
print('(B) Conditioning estimator on the variable V1 is P[X|V1 = v] = P[V1^2 + V2^2 <= 1|V1 =v] = P[V2^2<1-v^2]= intergal(-sqrt(1-v^2),sqrt(1-v^2))of 1/2) = sqrt(1-v^2)\n', Q3B(10000))
print('(C) Antithetic variables estimator variance of b is', Q3C(10000))
print('(D) Control variates estimator variance of U1 and U1^2 are', Q3D(10000))