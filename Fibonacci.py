# 1st Method : unMemoized
def Fibo_unMemo(n):
	if n < 0:
		print("N should be positive")
	elif n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return Fibo_unMemo(n-1) + Fibo_unMemo(n-2)



# 2nd Method : Memoized
cache = {0:0, 1:1}
def Fibo_Memo(n):
	if n < 0:
		print("N should be positive")
	elif n in cache:
		return cache[n]
	else:
		cache[n] = Fibo_Memo(n-1) + Fibo_Memo(n-2)

		return cache[n]
	



# Execution ===============================================================
from time import time

print("Fibo | Value | unMemo_Time | Memo_Time")
print("__________________________________")

for a in range(30, 40):
	# unMemo_Time
	t0 = time()
	s = Fibo_unMemo(a)
	t1 = time()
	temp1 = t1 - t0

	# Memo_Time
	t2 = time()
	s = Fibo_Memo(a)
	t3 = time()
	temp2 = t2 - t3

	print("%d | %d | %0.5f | %0.5f" % (s, a ,  t1 - t0, t2 - t3))













