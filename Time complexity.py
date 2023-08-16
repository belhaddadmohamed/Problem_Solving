def bubble_sort(arr):
	n = len(arr)

	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]


def merge(a,b):
    c=[]
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1

    if i==len(a):
        c.extend(b[j:])
    else:
        c.extend(a[i:])
    return c


def merge_sort(a):
    if len(a) <= 1:
        return a
    else:
        half = int(len(a)/2)
        left = merge_sort(a[:half])
        right = merge_sort(a[half:])

        return merge(left , right)
















#time complexity

def create_array(size, max):
    from random import randint
    return [randint(0,max) for _ in range(size)]


def benchmark(n = [100,200,300,400,500]):
	from time import time
	b0=[] #bubble sort times
	b1=[] #merge sort times

	for length in n:
		a = create_array(length , length)

		t0 = time()
		s  = merge_sort(a)  #Sort with Merge_sort
		t1 = time()
		b1.append(t1-t0)

		t0 = time()
		s  = bubble_sort(a)   #Sort with bubble_sort
		t1 = time()
		b0.append(t1-t0)

	print("n \t Merge_Sort \t Bubble_Sort")
	print("__________________________________")
	for i , cur_n in enumerate(n):
		print("%d \t %0.5f \t %0.5f" % (cur_n , b1[i] , b0[i]))



benchmark()

