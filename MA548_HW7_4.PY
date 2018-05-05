import numpy as np

# Inital variables
T = 1000
t = 0
V = 0 # Total trading volume until t
W = 0 # Total trading amount until t
PA = [51]   # Ask price at t
PB = [49]	# Bid price at t
PM = [50]	# Market price at t
X = np.zeros(101) 
X[46], X[47],X[48],X[50],X[51],X[52] = -1, -2, 3, 3, 2, 1
count_cancel = 0
total_lost_sales = 0
miu = 1
theta = 0.1
times = 0
while t <= T:
	PA_tempory = []
	PB_tempory = []
	for i in range(100):
		if X[i] > 0:
			PA_tempory.append(i)
		elif X[i] < 0:
			PB_tempory.append(i)
	if len(PA_tempory)>0:
		PA.append(min(PA_tempory))
	if len(PB_tempory)>0:
		PB.append(max(PB_tempory))
	PM.append((PA[-1]+PB[-1])/2) # Market price at t
	#Sub_1(miu,theta):
	lmd_S = np.sum(1/(p-PB[-1]) for p in range(PB[-1]+1,100))
	LS = np.random.exponential(lmd_S)   #Limit selling order
	tLS = t + LS #Limit selling order arrival time
	lmd_B = np.sum(1/(PA[-1]-p) for p in range(1, PA[-1]-1))
	LB = np.random.exponential(lmd_B)   #Limit buy order
	tLS = t + LS #Limit buy order arrival time
	M = np.random.exponential(2*miu)
	tM= t + M   #Next market order arrival time
	theta_S = np.sum(theta*abs(X[p]) for p in range(PA[-1],100))
	theta_B = np.sum(theta*abs(X[p]) for p in range(1,PB[-1]))
	C = np.random.exponential(theta_B+theta_S)       #Cancelation rate
	tC = t + C #Next cancelation arrival time
	Total_Probability = lmd_S + lmd_B + 2*miu + theta_B + theta_S
	N = np.random.exponential(Total_Probability)
	tN = t + N #Next event of all kinds happen time
	times += 1
	PMF = 0
	# Sub_2(miu,theta):
	U = np.random.uniform(0,1)
	U2 = np.random.uniform(0,1)
	if U <= lmd_S/Total_Probability:
		State =  1
		for p in range(PB[-1]+1,100):
			PMF +=1/((p-PB[-1])*lmd_S)
			if U2 <= PMF:
				break
	elif U <= (lmd_S+lmd_B)/Total_Probability:
		State =  2
		for p in range(1, PA[-1] -1):
			PMF +=1/((PA[-1]- p)*lmd_B)
			if U2 <= PMF:
				break
	elif U <= (lmd_S+lmd_B+2*miu)/Total_Probability:
		State =  3
		if U2 <= 1/2:
			p= PA[-1] 
		else:
			p= PB[-1]
	elif U <= (lmd_S+lmd_B+2*miu+theta_S)/Total_Probability:
		State =  4
		for p in range(PA[-1],100):
			PMF += theta*X[p]/theta_S
			if U2 <= PMF:
				break
	else:
		State =  5
		for p in range(1,PB[-1]):
			PMF += theta*abs(X[p])/theta_B
			if U2 <= PMF:
				break
	# Exact type:
	
	S = 1
	if State == 1:
		X[p] += 1
	elif State == 2:
		X[p] -= 1
	elif State == 3:
		X[PA[-1]] -= 1 
		V += S
		W += S*PA[-1] 
	elif State == 4:
		X[PB[-1]] += 1 
		V += S
		W += S*PA[-1]
		count_cancel += 1
		total_lost_sales += 1
	else:
		if X[p] > 0:
			X[p] -= 1
		elif X[p] < 0:
			X[p] += 1
		count_cancel += 1
	t = t + N


# Q1
print('[Question4]:\n')
print('Question a PA_AVG:\n',np.mean(PA),'\n')
print('Question a PB_AVG:\n',np.mean(PB),'\n')

# Q2
print('Question b\n W={}, V={}, W/V={}, V(T)/T = {}'.format(W,V,W/V,V/T),'\n')
# Q3
print('Question c\n C(T)={}, L(T)={}, C(T)/T={}'.format(count_cancel,total_lost_sales,count_cancel/T))







