import numpy as np
import math




def Q1A(NSim):
	l = 2	# arrival rate
	miu = 1	# service rate
	N = 10
	total_service = []
	for K in range(NSim):
		t = 0
		NA = 0
		ND = 0
		A = []
		D = []
		service_time = []
		n0 = 0;  # Initial number of customers
		n = n0;  
		U = np.random.uniform(0,1)
		if n > 0:
			tD = -np.log(U)/miu
		else:
			tD = np.inf
	 
		tA = -np.log(U)/l

		#Main algorithm
		while ND < N + n0:
	        
			if tA <= tD: 
				t = tA
				NA += 1
				n += 1
				U = np.random.uniform(0,1)
				tA = t - np.log(U)/l;   
				if n == 1:
					U = np.random.uniform(0,1)
					Y = -np.log(U)/miu
					tD = t + Y
				A.append(t)
		
			else:
				t = tD
				ND += 1
				n -= 1
				if n == 0:
					tD = np.inf
				else:
					U = np.random.uniform(0,1)
					Y = -np.log(U)/miu
					tD = t + Y
				D.append(t)

		for i in range(N):
			service_time.append(D[i]-A[i])

		total_service.append(np.sum(service_time))
	mm = np.mean(total_service)
	sigma = np.std(total_service, ddof = 1)
	return sigma**2,mm - 1.96 * sigma/(NSim**0.5), mm+ 1.96 * sigma/(NSim**0.5)



def Q1B(NSim):
	l = 2	# arrival rate
	miu = 1	# service rate
	N = 10
	total_service = []

	for K in range(NSim):
		U1 = []
		U2 = []
		# Generate Uniform List
		for i in range(100):
			UU = np.random.uniform(0,1)
			U1.append(UU)
			U2.append(1-UU)

		# This is for U part
		Ui = 0
		Uj = 50
		t = 0
		NA = 0
		ND = 0
		A = []
		D = []
		service_time = []
		n0 = 0;  # Initial number of customers
		n = n0;  
		
		if n > 0:
			tD = -np.log(U)/miu
		else:
			tD = np.inf

		U = U1[Ui]	
		Ui += 1
		tA = -np.log(U)/l

		#Main algorithm
		while ND < N + n0:
	        
			if tA <= tD: 
				t = tA
				NA += 1
				n += 1
				U = U1[Ui]	
				Ui += 1
				tA = t - np.log(U)/l;   
				if n == 1:
					U = U1[Uj]
					Uj += 1
					Y = -np.log(U)/miu
					tD = t + Y
				A.append(t)
		
			else:
				t = tD
				ND += 1
				n -= 1
				if n == 0:
					tD = np.inf
				else:
					U = U1[Uj]
					Uj += 1
					Y = -np.log(U)/miu
					tD = t + Y
				D.append(t)

		# This is for 1 - U part
		Ui = 0
		Uj = 50
		t = 0
		NA = 0
		ND = 0
		A2 = []
		D2 = []
		service_time = []
		n0 = 0;  # Initial number of customers
		n = n0;  
		
		if n > 0:
			tD = -np.log(U)/miu
		else:
			tD = np.inf

		U = U2[Ui]	
		Ui += 1
		tA = -np.log(U)/l

		#Main algorithm
		while ND < N + n0:
	        
			if tA <= tD: 
				t = tA
				NA += 1
				n += 1
				U = U1[Ui]	
				Ui += 1
				tA = t - np.log(U)/l;   
				if n == 1:
					U = U2[Uj]
					Uj += 1
					Y = -np.log(U)/miu
					tD = t + Y
				A2.append(t)
		
			else:
				t = tD
				ND += 1
				n -= 1
				if n == 0:
					tD = np.inf
				else:
					U = U2[Uj]
					Uj += 1
					Y = -np.log(U)/miu
					tD = t + Y
				D2.append(t)

		for i in range(N):
			service_time.append((D[i]-A[i]+D2[i]-A2[i])/2)

		total_service.append(np.sum(service_time))
	mm = np.mean(total_service)
	sigma = np.std(total_service, ddof = 1)
	return sigma**2,mm - 1.96 * sigma/(NSim**0.5), mm+ 1.96 * sigma/(NSim**0.5)

# Control variance with service time
def Q1C(NSim):
	l = 2	# arrival rate
	miu = 1	# service rate
	N = 10
	total_service = [] #This is total for whole time in a system, I just use wrong name, be careful
	total_yy = []# This is the real total time for service
	for K in range(NSim):
		t = 0
		NA = 0
		ND = 0
		A = []
		D = []
		service_time = []
		n0 = 0;  # Initial number of customers
		n = n0;  
		U = np.random.uniform(0,1)
		if n > 0:
			tD = -np.log(U)/miu
		else:
			tD = np.inf
	 
		tA = -np.log(U)/l
		YY = []
		#Main algorithm
		while ND < N + n0:
	        
			if tA <= tD: 
				t = tA
				NA += 1
				n += 1
				U = np.random.uniform(0,1)
				tA = t - np.log(U)/l
				if n == 1:
					U = np.random.uniform(0,1)
					Y = -np.log(U)/miu
					tD = t + Y
					YY.append(Y)
				A.append(t)
				
			else:
				t = tD
				ND += 1
				n -= 1
				if n == 0:
					tD = np.inf
				else:
					U = np.random.uniform(0,1)
					Y = -np.log(U)/miu
					tD = t + Y
					YY.append(Y)
				D.append(t)
				
		for i in range(N):
			service_time.append(D[i]-A[i])
		total_yy.append(np.sum(YY[:10]))
		total_service.append(np.sum(service_time))
	# Compute the C*
	Cov_C = -np.cov(total_service, total_yy,ddof=1)[0][1]
	C_star = Cov_C/np.var(total_yy,ddof =1)
	C = []
	for i in range(NSim):
		C.append(total_service[i]+C_star*(total_yy[i]-10))

	mm = np.mean(C)
	sigma = np.std(C, ddof = 1)
	return sigma**2,mm - 1.96 * sigma/(NSim**0.5), mm+ 1.96 * sigma/(NSim**0.5)


def Q1D(NSim):
	l = 2	# arrival rate
	miu = 1	# service rate
	N = 10
	total_service = [] #This is total for whole time in a system, I just use wrong name, be careful
	total_yy = []# This is the real total time for service
	for K in range(NSim):
		t = 0
		NA = 0
		ND = 0
		A = []
		D = []
		service_time = []
		n0 = 0;  # Initial number of customers
		n = n0;  
		U = np.random.uniform(0,1)
		if n > 0:
			tD = -np.log(U)/miu
		else:
			tD = np.inf
	 	
		tA = -np.log(U)/l
		YY = []
		AA = [tA]
		#Main algorithm
		while ND < N + n0:
	        
			if tA <= tD: 
				t = tA
				NA += 1
				n += 1
				U = np.random.uniform(0,1)
				a =	 -np.log(U)/l
				tA = t + a
				AA.append(a)
				if n == 1:
					U = np.random.uniform(0,1)
					Y = -np.log(U)/miu
					tD = t + Y
					YY.append(Y)

				A.append(t)
				
			else:
				t = tD
				ND += 1
				n -= 1
				if n == 0:
					tD = np.inf
				else:
					U = np.random.uniform(0,1)
					Y = -np.log(U)/miu
					tD = t + Y
					YY.append(Y)
				D.append(t)
				
		for i in range(N):	
			service_time.append(D[i]-A[i])
		total_yy.append(np.sum(YY[:10])-np.sum(AA[:10]))
		total_service.append(np.sum(service_time))
	# Compute the C*
	Cov_C = -np.cov(total_service, total_yy,ddof=1)[0][1]
	C_star = Cov_C/np.var(total_yy,ddof =1)
	C = []
	for i in range(NSim):
		C.append(total_service[i]+C_star*(total_yy[i]-5))

	mm = np.mean(C)
	sigma = np.std(C, ddof = 1)
	return sigma**2,mm - 1.96 * sigma/(NSim**0.5), mm+ 1.96 * sigma/(NSim**0.5)

def Q1E(NSim):
	l = 2	# arrival rate
	miu = 1	# service rate
	N = 10
	total_service = []
	Ni = []
	for K in range(NSim):
		t = 0
		NA = 0
		ND = 0
		A = []
		D = []
		service_time = []
		n0 = 0;  # Initial number of customers
		n = n0;  
		U = np.random.uniform(0,1)
		if n > 0:
			tD = -np.log(U)/miu
		else:
			tD = np.inf
	 	
		tA = -np.log(U)/l
		Ni.append(n)
		#Main algorithm
		while ND < N + n0:
	        
			if tA <= tD: 
				t = tA
				NA += 1
				n += 1
				U = np.random.uniform(0,1)
				tA = t - np.log(U)/l
				Ni.append(n) 
				if n == 1:
					U = np.random.uniform(0,1)
					Y = -np.log(U)/miu
					tD = t + Y
				A.append(t)
		
			else:
				t = tD
				ND += 1
				n -= 1
				if n == 0:
					tD = np.inf
				else:
					U = np.random.uniform(0,1)
					Y = -np.log(U)/miu
					tD = t + Y
				D.append(t)

		for i in range(N):
			service_time.append(D[i]-A[i])

		total_service.append(np.sum(service_time))
	mm = np.mean(total_service)
	sigma = np.std(Ni, ddof = 1)
	return sigma**2,mm - 1.96 * sigma/(NSim**0.5), mm+ 1.96 * sigma/(NSim**0.5)


def Q2A(n, l):
	N = 0
	Xj = []
	for i in range(n):
		L = 0
		N = np.random.geometric(1/3)
		for j in range(N):
			# intergration is -2(sqrt(x)+1)*exp(-sqrt(x))
			U = np.random.uniform(0,1)
			L += (np.log(U))**2
		if L  > l:
			Xj.append(1)
		else:
			Xj.append(0)
	m = np.mean(Xj)
	sigma = np.std(Xj, ddof = 1)
	return sigma**2,m - 1.96 * sigma/(n**0.5), m + 1.96 * sigma/(n**0.5)


def Q2B(n,l,m):
    N = 0
    P = []
    p = 1/3
    nn = []
    L = 0
    Xi = []
    estimator = []
    for Y in range(1,m+1):
        Xj = [0]
        if Y == 1:
            P.append(p)
            nn.append(np.int(n*P[-1]))
            for i in range(nn[-1]):
                U = np.random.uniform(0,1)
                L = (np.log(U))**2
                if L  > l:
                    Xj.append(1)
                else:
                    Xj.append(0)

            Xi.append(np.mean(Xj))
        elif Y != m:
            P.append(((1-p)**(Y-1))*p)
            nn.append(np.int(n*P[-1]))
            Xj = [0]
            for i in range(nn[-1]):
                L = 0
                for j in range(Y):
                    U = np.random.uniform(0,1)
                    L += (np.log(U))**2

                if L  > l:
                    Xj.append(1)
                else:
                    Xj.append(0)
            Xi.append(np.mean(Xj))
        else:
            P.append((1-p)**(m-1))
            nn.append(np.int(n*P[-1]))
            Xj = [0]
            for i in range(nn[-1]):
                L = 0
                N = np.random.geometric(p) + Y - 1
                for j in range(N):
                    U = np.random.uniform(0,1)
                    L += (np.log(U))**2

                if L  > l:
                    Xj.append(1)
                else:
                    Xj.append(0)
            Xi.append(np.mean(Xj))

    for i in range(m):
    	estimator.append(P[i]*Xi[i])

    mm = np.sum(estimator)
    sigma = np.std(estimator,ddof=1)
    
    return sigma**2,mm - 1.96 * sigma/(m**0.5), mm + 1.96 * sigma/(m**0.5)

print("[Question 1]\n")
print('[A] Raw simulation estimator\n',Q1A(10000))
print('[B] Antithetic variables\n',Q1B(10000))
print('[C] Control variate with Si,\n',Q1C(10000))
print('[D] Control variate with Si - Ai,\n',Q1D(10000))
print('[E] Conditional expection with Ni,\n',Q1E(10000))
print("\n[Question 2]\n")
print('[A] Crude Monte Carlo Variance and CI is :', Q2A(100000,15))

print('\n[B] Stratified sampling estimator Variance and CI is :', Q2B(100000,15,50))

