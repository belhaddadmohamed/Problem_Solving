# 1st method : Recursion
def Fibonacci_unMemoized(n):
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return Fibonacci_unMemoized(n-1) + Fibonacci_unMemoized(n-2)



# 2nd method : Dynamic programming
cache = {0:0, 1:1}
def Fibo_Memo(n):
	if n in cache:
		return cache[n]
		
	cache[n] = Fibo_Memo[n-1] + Fibo_Memo[n-2]
	return cache[n]
	


# Execution
from time import time
print("Fn \t Valeur \t Temps_sans_mémoisation \t Temps_avec_mémoisation")
print("__________________________________")
for a in range(30,50):
	t0 = time()
	s = Fibonacci_unMemoized(a)
	t1 = time()
	temp1 = t1 - t0

	t2 = time()
	s = Fibonacci_Memoized(a)
	t3 = time()
	temp2 = t2 - t3

	print("%d \t %d \t %0.5f \t %0.5f" % (s, a ,  t1 - t0, t2 - t3))













