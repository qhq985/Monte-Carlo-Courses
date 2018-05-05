import numpy as np 
from scipy.stats import gamma, norm, lognorm
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')



def expweibull(rho):
	l = 2 
	a = 2
	b = 3
	N = 100000
	miu = np.array([0 , 0])
	corr = np.array([[1, rho],[rho, 1]])
	Z = np.random.multivariate_normal(miu, corr, N)
	U = norm.cdf(Z)
	X = (-1/l)*np.log(U[:,0])
	Y = b*(-np.log(U[:,1]))**(1/a)
	corre = np.corrcoef(X,Y)

	plot1 = plt.subplot2grid((2, 2), (1, 0))
	plot2 = plt.subplot2grid((2, 2), (0, 0), colspan = 2)
	plot3 = plt.subplot2grid((2, 2), (1, 1))

	plot1.plot(X,Y, '.')
	plot2.hist(X, bins=30)
	plot3.hist(Y, bins=30, orientation = 'horizontal')
	plot2.set_title('Case 1, rho={}'.format(rho))
	plt.show()



	print("Case1, rho=", rho,"\n",corre[0][1])

def gammalognorm(rho):
	l = 3
	a = 6.7
	N = 100000
	miu = np.array([0 , 0])
	corr = np.array([[1, rho],[rho, 1]])
	Z = np.random.multivariate_normal(miu, corr, N)
	U = norm.cdf(Z)
	X = gamma.ppf(U[:, 0], a, l)
	Y = lognorm.ppf(U[:, 1], 0.1, 0.05)
	corre = np.corrcoef(X,Y)

	plot1 = plt.subplot2grid((2, 2), (1, 0))
	plot2 = plt.subplot2grid((2, 2), (0, 0), colspan = 2)
	plot3 = plt.subplot2grid((2, 2), (1, 1))

	plot1.plot(X,Y, '.')
	plot2.hist(X, bins=30)
	plot3.hist(Y, bins=30, orientation = 'horizontal')
	plot2.set_title('Case 2, rho={}'.format(rho))
	plt.show()

	print("Case2, rho=", rho,"\n",corre[0][1])


expweibull(0.8)
expweibull(0.2)
expweibull(-0.8)

gammalognorm(0.8)
gammalognorm(0.2)
gammalognorm(-0.8)

