import random, timeit
## 여기에 세 가지 정렬함수를 위한 코드를...


def quick_sort(A, start, end):
	global Qc
	global Qs
	
	if start >= end:
		return
	pivot = start #피벗 초기값은 첫번째 요소
	left, right = start+1, end
	
	while left <= right:
		#Qc, Qs = 0,0
		# 피벗보다 큰 데이터를 찾을 때까지 반복
		while left <= end and A[left] <= A[pivot]:
			left+=1
			Qc+=1
		#피벗보다 작은 데이터를 찾을 때까지 반복
		while right > start and A[right] >= A[pivot]:
			right-=1
			Qc+=1
		if left>right: # 엇갈렸다면 작은 right -=1 데이터와 피벗을 교체
			A[right], A[pivot] = A[pivot], A[right]
			Qs+=1
		else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체 
			A[left], A[right] = A[right],A[left]
			Qs+=1
	# 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
	quick_sort(A, start, right-1)
	quick_sort(A, right+1, end)
	return A


def merge_sort(A, first, last):
	
	if first >= last: return

	m = (first + last)//2
	
	merge_sort(A, first, m)
	merge_sort(A, m+1, last) 
	merge_two_sort(A, first, last)
	return A
	
def merge_two_sort(A, first, last):
	global Mc
	global Ms
	
	m = (first + last)//2
	i, j = first, m + 1
	B = []
	
	while i <= m and j <= last:
		if A[i] <= A[j]:
			B.append(A[i])
			i+=1
			Mc+=1
		else:
			B.append(A[j])
			j+=1
			Mc+=1
	for k in range(i, m+1):
		B.append(A[k])
		#Ms+=1
		
	for k in range(j, last+1):
		B.append(A[k])
		#Ms+=1
		
	for i in range(first, last+1):
		A[i] = B[i - first]
		Ms+=1
	

def heapify(A,n,i):
	l = 2 * i + 1
	r = 2 * i + 2
	
	global Hc
	global Hs
	
	if l < n and A[l] > A[i]:
		largest = l
		Hc+=1
	else:
		largest = i
		Hc+=1
		
	if r < n and A[r] > A[largest]:
		largest = r
		Hs+=1
	
	if largest != i:
		A[i], A[largest] = A[largest], A[i]
		Hs+=1
		heapify(A, n, largest)
		
		
def heap_sort(A):
	n = len(A)
	global Hs
	
	for i in range(n, -1,-1):
		heapify(A, n, i)
		
	for i in range(n-1,0,-1):
		A[0] ,A[i] = A[i], A[0]
		Hs+=1
		heapify(A, i, 0)	



# 아래 코드는 바꾸지 말 것!
# 직접 실행해보면, 어떤 값이 출력되는지 알 수 있음
#

def check_sorted(A):
	for i in range(n-1):
		if A[i] > A[i+1]: return False
	return True

#
# Qc는 quick sort에서 리스트의 두 수를 비교한 횟수 저장
# Qs는 quick sort에서 두 수를 교환(swap)한 횟수 저장
# Mc, Ms는 merge sort에서 비교, 교환(또는 이동) 횟수 저장
# Hc, Hs는 heap sort에서 비교, 교환(또는 이동) 횟수 저장

Qc, Qs, Mc, Ms, Hc, Hs = 0, 0, 0, 0, 0, 0

n = int(input())
random.seed()
A = []
for i in range(n):
    A.append(random.randint(-1000,1000))
B = A[:]
C = A[:]

print("")
print("Quick sort:")
print("time =", timeit.timeit("quick_sort(A, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Qc, Qs))

print("Merge sort:")
print("time =", timeit.timeit("merge_sort(B, 0, n-1)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Mc, Ms))


print("Heap sort:")
print("time =", timeit.timeit("heap_sort(C)", globals=globals(), number=1))
print("  comparisons = {:10d}, swaps = {:10d}\n".format(Hc, Hs))

# 진짜 정렬되었는지 check한다. 정렬이 되지 않았다면, assert 함수가 fail됨!
assert(check_sorted(A))
assert(check_sorted(B))
assert(check_sorted(C))


