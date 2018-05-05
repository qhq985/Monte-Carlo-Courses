import numpy as np

#Initial the variables
t, NA, ND = 0, 0, 0
n = 0
tD = np.inf
T = 10
ID = 0
l = 0.8
U = np.random.uniform(0,1)
tA = 0
tD = 0
tF = 0
A = 0
miu = 1
R = []
t_sojurn = 0


while t<T:

	

	#Case 1:
	if tA<=tD and tA<=T:
		if n!=0:
			w = (tA - t)/n
			R = [i - w for i in R]
		A += (tA - t)*n
		n += 1
		t = tA
		NA += 1
		y = np.random.exponential(miu)
		R.append(y)
		U = np.random.uniform(0,1)
		tA = tA - np.log(U)/l
		R.sort
		tD = t + R[0]*n
		
	# Case 2
	elif tD < tA and tD < T:#Next event is a departure
		A += (tD - t)*n
		n -= 1
		ND += 1
		if n==0:
			if tA <= T:
				tF += (tA - t)
			else:
				tF += (T - t)
			t = tD
			tD = np.inf

		else:
			R.pop(0)
			w = (tD - t)/(n+1)
			R = [i - w for i in R]
			t = tD
			tD = t + R[0]*n
	elif  min(tA, tD)> T and n>0: #Next event occurs after time T, but there still customers in the system
		if n == 0:
			if tA <= T:
				tF += (tA - t)
			else:
				tF += (T - t)
			tP = max(t-T,0)
			break
		else:
			n -= 1
			ND += 1
			R.pop(0)
			w = (tD -t)/(n+1)
			R = [i - w for i in R]
			t = tD
			tD = t +R[0]*n
		A = A + (T - t)*n
		S = tS + (T - t)* n
		t_sojurn = tS - (T - max(A))
		t = T
print('[Question1]:\n')
print('2.i Long-run proportion of time the server is idling:',tF/T,'\n')
print('2.ii Long-run average number of customers in the system:',A/T,'\n')
print('2.iii Long-run average sojourn times',t_sojurn/ND, '\n')


