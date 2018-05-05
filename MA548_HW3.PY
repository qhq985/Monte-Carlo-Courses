from random import randint  
import numpy as np
import math

def Q1(n): 
	count = 0
	for i in range(1,n):
		num = 0
		result = []
		while len(result)<11:
			dice1 = randint(1,6)
			dice2 = randint(1,6)
			sum = dice1 + dice2 
			if sum not in result:
				result.append(sum)
			num += 1
		count += num
	return count/n

def Q3A(n):
	count = 0
	for i in range(1,n):
		sum = 0
		j = 0
		while sum <= 1:
			U = np.random.uniform(0,1)
			sum = sum + U
			j += 1
		count = count + j
	return count/n

def Q3B(n,lamta):
	count = 0
	for i in range(1,n):
		sum = 1
		j = 0
		while sum >= math.exp(-lamta):
			U = np.random.uniform(0,1)
			sum = sum * U
			j += 1
		count = count + j - 1
	return count/n

def Q4C(n):
	count = 0
	for j in range(1,n):
		P = [0.05, 0.1, 0.2, 0.3, 0.9, 1.0]
		U = np.random.uniform(0,1)
		t = len(P)
		for i in range(0,t):
			if U <= P[i]:
				break
		count += i + 1 
	return count/n

def Q4E(n):
	count = 0
	for j in range(1,n):
		P = [0.6, 0.7, 0.8, 0.9, 0.95, 1.0]
		U = np.random.uniform(0,1)
		t = len(P)
		for i in range(0,t):
			if U <= P[i]:
				break
		count += i + 1 
	return count/n

print("\n[Question 1] \n")
for i in range(2,5):
	print("n=",pow(10,i), ":", Q1(pow(10,i)))

print("\n[Question 3A] \n")
for i in range(2,5):
	print("n=",pow(10,i), ":", Q3A(pow(10,i)))

print("\n[Question 3B] \n")
print("For lamta = 1\n")
for i in range(2,5):
	print("n=",pow(10,i), ":", Q3B(pow(10,i),1))
print("\nFor lamta = 2\n")
for i in range(2,5):
	print("n=",pow(10,i), ":", Q3B(pow(10,i),2))

print("\n[Question 4C] \n")
print("E[N] is", Q4C(10000))

print("\n[Question 4E] \n")
print("E[N] is", Q4E(10000))