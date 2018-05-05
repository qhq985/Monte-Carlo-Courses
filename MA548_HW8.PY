import numpy as np
import math 


def SSP1():
	S = []
	S.append(np.random.normal(0,1))
	S.append(np.random.normal(0,1))
	S2 = np.var(S,ddof =1)
	X_mean = [np.mean(S)]
	i = 2
	while np.sqrt(S2/i) + 1/i > 0.01:
		S.append(np.random.normal(0,1))
		X_mean.append(X_mean[-1] + (S[-1]-X_mean[-1])/(i+1))
		S2 = (1-1/i)*S2 + (i+1)*((X_mean[-1] -X_mean[-2])**2)
		i += 1
	return i

def SSP2():
	S = []
	S.append(np.random.normal(0,1))
	S.append(np.random.normal(0,1))
	S2 = np.var(S,ddof =1)
	X_mean = [np.mean(S)]
	i = 2
	while np.sqrt(S2/i) + 1/i**2 > 0.01:
		S.append(np.random.normal(0,1))
		X_mean.append(X_mean[-1] + (S[-1]-X_mean[-1])/(i+1))
		S2 = (1-1/i)*S2 + (i+1)*((X_mean[-1] -X_mean[-2])**2)
		i += 1
	return i

def Smooth_Func_ExpecationsA(n):
	S = []
	S2 = []
	gxy = []
	for i in range(n):
		t = np.random.normal(0,1)
		S.append(t)
		S2.append(t**2)
	X = np.mean(S)
	Y = np.mean(S2)
	# sigmaX = np.var(S, ddof = 1)
	# sigmaY = np.var(S2, ddof = 1)
	# cov = np.cov(S,S2, ddof =1)[0][1]
	# sigma2 = (-2*X)**2*cov + 
	for i in range(n):
		gxy.append(((-2*X)*(S[i]-X)+(S2[i]-Y))**2)
	sigma2 = np.sum(gxy)/(n-1)
	estimate = [(Y - X**2) - 1.96*np.sqrt(sigma2/n), (Y - X**2) + 1.96*np.sqrt(sigma2/n)]
	real = np.var(S, ddof =1)

	return real, estimate

def Smooth_Func_ExpecationsB(n):
	S1 = []
	S2 = []
	S3 = []
	gxy = []
	for i in range(n):
		t1 = np.random.normal(0,1)
		t2 = np.random.uniform(0,1)
		S1.append(t1)
		S2.append(t2)
		S3.append(t1*t2)
	X = np.mean(S1)
	Y = np.mean(S2)
	Z = np.mean(S3)

	for i in range(n):
		gxy.append(((-Y)*(S1[i]-X)+(-X)*(S2[i]-Y)+(S3[i]-Z))**2)
	sigma2 = np.sum(gxy)/(n-1)
	estimate = [(Z - X*Y) - 1.96*np.sqrt(sigma2/n), (Z - X*Y) + 1.96*np.sqrt(sigma2/n)]
	real = np.cov(S1,S2, ddof =1)[0][1]

	return real, estimate

def Smooth_Func_ExpecationsC(n):
	S1 = []
	S2 = []
	gxy = []
	for i in range(n):
		t1 = np.random.normal(0,1)
		t2 = np.random.uniform(0,1)
		S1.append(t1)
		S2.append(t2)
	X = np.mean(S1)
	Y = np.mean(S2)

	for i in range(n):
		gxy.append(((1/Y)*(S1[i]-X)+(-X/(Y**2))*(S2[i]-Y))**2)
	sigma2 = np.sum(gxy)/(n-1)
	estimate = [(X/Y) - 1.96*np.sqrt(sigma2/n), (X/Y) + 1.96*np.sqrt(sigma2/n)]
	real = X/Y

	return real, estimate
def Sequence_a():
	U = []
	U1 = np.random.uniform(0,1)
	n = 2
	U.append(U1)
	U2 = np.random.uniform(0,1)
	U.append(U2)
	while U[-2] <= U[-1]:
		U.append(np.random.uniform(0,1))
		n += 1
	return n

def Sequence_b(n):
	M = [0]
	for i in range(n):
		M.append(1/math.factorial(i))
	return np.sum(M)


def Sequence_c():
	M = []
	n = 2
	M.append(Sequence_b(100))
	M.append(Sequence_b(100))
	while 1.96*np.sqrt(np.var(M,ddof =1)/n) + 1/n > 0.001:
		n += 1
		M.append(Sequence_b(100))
	return n
print('[Question2C]:\n1/n:', SSP1())

print('\n1/n^2:', SSP2())

print('[Question3A:]')
print('I use normal distribution here')
print('Real_value AND Estimate CI are\n',format(Smooth_Func_ExpecationsA(10000)))

print('\n[Question3B:]')
print('I use normal distribution and uniform distribution(iid.) here')
print('Real_value AND Estimate CI are\n',format(Smooth_Func_ExpecationsB(10000)))

print('\n[Question3C:]')
print('I use normal distribution and unidorm distribution(iid.) here')
print('Real_value AND Estimate CI are\n',format(Smooth_Func_ExpecationsC(10000)))
print('\n[Question4A]:\n', Sequence_a())

print('\n[Question4B]:\n')
print('N = 10: ',Sequence_b(10),'\n')
print('N = 100: ',Sequence_b(100),'\n')
print('N = 1000: ',Sequence_b(1000),'\n')

print('[Question4C]:\n')
print('N =',Sequence_c())
