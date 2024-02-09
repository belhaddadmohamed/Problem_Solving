# Recursion
def Fibonacci_unMemoized(n):
	if n < 0:
		print("Incorrect input")
	elif n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return Fibonacci_unMemoized(n-1) + Fibonacci_unMemoized(n-2)

print(Fibonacci_unMemoized(4))


# Dynamic programming
FibArray = [0, 1]
def Fibonacci_Memoized(n):
	if n <= 0:
		print("Incorrect input")
	elif n <= len(FibArray):
		return FibArray[n - 1]
	else:
		temp_fib = Fibonacci_Memoized(n - 1) + Fibonacci_Memoized(n - 2)
		FibArray.append(temp_fib)
		return temp_fib

print(Fibonacci_Memoized(9))




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













