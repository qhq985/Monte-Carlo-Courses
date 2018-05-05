import numpy.random
import sympy
import numpy
import math
import sys
from scipy import integrate
from scipy.integrate import quad

def q1(Z0,n):
	Z=Z0
	for i in range(1,n+1):
		Z2 = Z**2
		t = Z2%1000000
		Z = t//100
		U = Z/10000
		print("U{} is {}".format(i,U))

def q2(m,a,c,Z0,n):
	Z=Z0
	for i in range(0,n+1):
		print("Z{} is {}".format(i,Z))
		Z = (a*Z+c)%m

def q3(X1,X2,n):
		print("X1 is {}".format(X1))
		print("X2 is {}".format(X2))
		for i in range(3,n+1):
			X = (5*X1+3*X2)%100
			print("X{} is {}".format(i,X))
			X1 = X2
			X2 = X

def q4A(n):
	return numpy.sum(numpy.exp(numpy.exp(numpy.random.uniform(0,1,n))))/n

def q4AC(x):
	return numpy.exp(numpy.exp(x))

def q4B(n):
	x = numpy.random.uniform(-2,2,n)
	return 4*numpy.sum(numpy.exp(x+x**2))/n

def q4BC(x):
	return numpy.exp(x+x**2)

def q4C(n):
	x = numpy.random.uniform(0,1,n)
	y = 1/x
	return 2*numpy.sum(numpy.exp(-(y-1)**2)*y**2)/n

def q4CC(x):
	return numpy.exp(-x**2)

def q4D(n):
	x = numpy.random.uniform(0,1,n)
	y =	numpy.random.uniform(0,1,n)
	return numpy.sum(numpy.exp((x+y)**2))/n

def q4DC(x,y):
	return  numpy.exp((x+y)**2)

def q5(n):
	x = numpy.random.uniform(0,1,n)
	return numpy.mean((x-.5)*numpy.exp(x))

def q6A(n):
	u = numpy.random.uniform(0,1,n)
	v = numpy.sqrt(1-u**2)
	return (numpy.mean(u*v)-numpy.mean(u)*numpy.mean(v))/numpy.sqrt(numpy.var(u)*numpy.var(v))

def q6B(n):
	u = numpy.random.uniform(0,1,n)
	v = numpy.sqrt(1-u**2)
	return (numpy.mean((u**2)*v)-numpy.mean(u**2)*numpy.mean(v))/numpy.sqrt(numpy.var(u**2)*numpy.var(v))


print("MA548\nHW2\nHangquan Qian\n1/29/18")
print("\n[Question 1A] \n ")
q1(7182,20)
print("\n[Question 1B] \n")
q1(1009,30)
print("\n[Question 2] \n")
q2(16,5,3,7,20)
print("\nYes, this LCG has a full cycle, each 15 numbers are a combo")
print("\n[Question 3] \n")
q3(23,66,14)
print("\n[Question 4A] \n")
for i in range(1,6):
	print(pow(10,i), ":", q4A(pow(10,i)))
print("Exact Answer:", quad(q4AC,0,1))
print("\n[Question 4B] \n")
for i in range(1,6):
	print(pow(10,i), ":", q4B(pow(10,i)))
print("Exact Answer:", quad(q4BC,-2,2))
print("\n[Question 4C] \n")
for i in range(1,6):
	print(pow(10,i), ":", q4C(pow(10,i)))
print("Exact Answer:", quad(q4CC,-numpy.inf,numpy.inf))
print("\n[Question 4D] \n")
for i in range(1,6):
	print(pow(10,i), ":", q4D(pow(10,i)))
print("Exact Answer:", integrate.nquad(q4DC,[[0,1],[0,1]]))
print("\n[Question 4E] \n\n\n\n\n")
print("\n[Question 5] \n")
for i in range(1,6):
	print(pow(10,i), ":", q5(pow(10,i)))
print("\nExact Answer:\n\n\n\n\n\n\n\n\n")
print("\n[Question 6A] \n")
for i in range(1,6):
	print(pow(10,i), ":", q6A(pow(10,i)))
print("\n[Question 6B] \n")
for i in range(1,6):
	print(pow(10,i), ":", q6B(pow(10,i)))
