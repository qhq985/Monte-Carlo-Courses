import numpy as np


def DMG(a, c, l):
	Remain_dmg = 0
	t = [0]
	Total_dmg  = 0
	X = [0]
	while  Total_dmg <= c:
		U = np.random.uniform(0,1)
		t.append(t[-1] - np.log(U)/l)
		Remain_dmg = 0
		for i in range((len(t))-1):
			Remain_dmg += X[i]*np.exp(-a*(t[-1]-t[i]))
		X.append(np.random.gamma(2,1))
		Total_dmg = Remain_dmg + X[-1]
	return t[-1]


count = 0
K = 1000
for i in range(K):
	count += DMG(0.5,5,1)
print('\n[Question3]:',count/K)