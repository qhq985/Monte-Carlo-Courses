import numpy as np

#Initial the variables
l = 0.8
miu = 1
T = 10000
t, NA, ND = 0, 0, 0 
n = 0
tA = 0
tD = np.inf
tS = 0
A = []
D = []
t_sojurn = 0
tF = 0


while t<T:
	#Initialize simulation
	 #times of sojurn times(waiting time + service times)

	if n==0:
		if tA <= T:
			tF += (tA - t)
		else:
			tF += (T - t)

	#Case 1
	if tA <= tD and tA <= T:  #Next event is an arrival
		tS = tS + (tA - t) * n 
		t = tA
		NA = NA + 1 #Number of arrvial
		n += 1 #Number of customers
		A.append(t)
		U1 = np.random.uniform(0,1)
		tA = t - np.log(U1)/l
		if n == 1:  #If only one customer now
			U2 = np.random.uniform(0,1) #System was empty prior to this arrival
			Y =  -np.log(U2)/l
			tD = t + Y
			D.append(tD - max(A))

	#Case 2
	elif tD < tA and tD < T: #Next event is a departure
		tS = tS + (tD - t)*n
		t = tD
		ND += 1 #Number of departure
		n -= 1
		if n == 0:
			tD = np.inf
		elif n>0:
			U = np.random.uniform(0,1)
			Y =  -np.log(U)/l 
			tD = t + Y
			D.append(tD - max(A))

	#Case 3
	elif  min(tA, tD)> T and n>0: #Next event occurs after time T, but there still customers in the system
		tS = tS + (T - t)* n
		t_sojurn = tS - (T - max(A))
		t = T
print('[Question2]:\n')
print('2.i Long-run proportion of time the server is idling:',tF,'\n')
print('2.ii Long-run average number of customers in the system:',tS/T,'\n')
print('2.iii Long-run average sojourn times',t_sojurn/ND, '\n')

	