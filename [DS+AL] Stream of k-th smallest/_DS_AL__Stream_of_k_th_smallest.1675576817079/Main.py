
# heap 큐 알고리즘을 이용하였다. 
#힙은 모든 부모 노드가 자식보다 작거나 같은 값을 갖는 이진 트리입니다. 
#이 구현에서는 모든 k에 대해 heap[k] <= heap[2*k+1]과 heap[k] <= heap[2*k+2]인 배열을 사용합니다.
#0부터 셉니다
#비교를 위해, 존재하지 않는 요소는 무한으로 간주합니다
#heapq.nsmallest(n, iterable, key=None)
#iterable에 의해 정의된 데이터 집합에서 n 개의 가장 작은 요소로 구성된 리스트를 반환합니다
#
#시간 복잡도
#아래 과정은 전체적으로 살펴보면 n번 n/2번 n/4번 ....으로 동작합니다.
#따라서 전체 시간을 T(Q)라 가정하면 
#T(Q) = N+ N/2+ N/4 + ...
# n = 1*2^x
#logn = xlog2
#logn = x
#O(log n)



import heapq
from heapq import heappush, heappop

heap = []
sum = 0 #최종값

# 입력 받기 
nums = list(map(int, input().split()))

for i in range(len(nums)):
	k = (i // 3 + 1)
	heappush(heap, nums[i]) #heap모듈에 num[i]를 힙에 추가한다.
	p = heapq.nsmallest(k, heap)#k번째 원소값 구하기 
    # print(p[-1], p)
	sum += p[-1] 

print(sum)
"""
import heapq 

def heap_sort(nums):
	heap = []
	for num in nums:
		heapq.heappush(heap, num)   
		
	sorted_nums = []  
	#print(sorted_nums)
	while heap:    
		sorted_nums.append(heapq.heappop(heap)) 
	n.append(sorted_nums[k-1])
	return sorted_nums 
#print(heap_sort([4, 1, 7, 3, 8, 5]))
if __name__ == '__main__':
	nums = list(map(int,input().split()))
	m = []
	n = []#출력값
	
	for i in range(len(nums)):
		m.append(nums[i])
		#`k`는 매 라운드마다 업데이트한다.
		k = (i)//3+1
		heap_sort(m)
		#n.append(m[k-1])
	#print(heap_sort(m))
	print(sum(n))



from random import randint

def swap(m, i, j): #변수를 바꾸는 함수 
	temp = m[i]
	m[i] = m[j]
	m[j] = temp

def part(m, left, right, pIndex):
	# 목록에서 `pIndex`를 피벗으로 선택
	pivot = m[pIndex]
	
	# 피벗을 끝으로 이동
	swap(m, pIndex, right)
	
	# 피벗보다 작은 # 요소는 `pIndex`의 왼쪽으로 푸시됩니다.
	# 피벗보다 많은 # 요소는 `pIndex`의 오른쪽으로 푸시됩니다.
	# 등가 요소는 어느 쪽이든 갈 수 있습니다.
	pIndex = left
	
	# 피벗, `pIndex`보다 작거나 같은 요소를 찾을 때마다
	#가 증가하고 해당 요소는 피벗 앞에 배치됩니다.
	for i in range(left, right):
		if m[i] <= pivot:
			swap(m, i, pIndex)
			pIndex = pIndex + 1

	# 피벗을 제자리로 이동
	swap(m, pIndex, right)
	
	#는 `pIndex`(피벗 요소의 인덱스)를 반환합니다.
	return pIndex

# `left… right` 내의 목록에서 `k` 가장 작은 요소를 반환합니다.
#(즉, left <= k <= right). 목록 내의 검색 공간과 목록크기는 라운드마다 변경된다.
def quickSelect(m, left, right,k):

	# 목록에 요소가 하나만 포함되어 있으면 해당 요소를 반환합니다.
	if left == right:
		n.append(m[k])
		return m[left]

	
	# 왼쪽과 오른쪽 사이 `pIndex` 선택
	pIndex = randint(left, right)
	pIndex = part(m, left, right, pIndex)

	
	# 피벗이 정렬된 위치에 있습니다.
	if k == pIndex:
		n.append(m[k])
		return m[k]


	# `k`가 피벗 인덱스(pIndex)보다 작은 경우
	elif k < pIndex:
		return quickSelect(m, left, pIndex - 1,k)


	# `k`가 피벗 인덱스(pIndex)보다 큰 경우 
	else:
		return quickSelect(m, pIndex + 1, right,k)


if __name__ == '__main__':
	nums = list(map(int,input().split()))
	m = []
	n = []#출력값
	
	for i in range(len(nums)):
		m.append(nums[i])
		#`k`는 매 라운드마다 업데이트한다.
		k = (i)//3+1
		quickSelect(m, 0, len(m)-1,k-1)

	print(sum(n))
#quick select 알고리즘은 Quick Sort의 원리를 이용하여 만든 알고리즘입니다. 
#정렬을 한 뒤 k 번째 요소를 찾는 것은 전체 시간 복잡도가 정렬에 따라가기 때문에 worst case 가 O (n log n) 또는 O(n^2)가 됩니다. 
#하지만 Quick Selection의 경우 worst case 가 O(n) 이 됩니다.
# 수행시간 
# 아래 과정은 전체적으로 살펴보면 n번 n/2번 n/4번 ....으로 동작합니다.
#따라서 전체 시간을 T(Q)라 가정하면 
#T(Q) = N+ N/2+ N/4 + ...
#T(Q/2) = N/2+ N/4 + ...
#T(Q) - T(Q/2) = N
#T(Q) = 2N = O(N)
	

#

#
import heapq
from heapq import heappush, heappop

heap = []
sum = 0

nums = list(map(int,input().split()))

for i in range(len(nums)):
	#m.append(nums[i])
	k = (i//3+1)
	heappush(heap,nums[i])
	p = heapq.nsmallest(k, heap)
	#p = nth_smallest(heap.copy(),k)
	sum += p[-1]
	
print(sum)


# import numpy as np

# heap = []
# sum = 0

# num = list(map(int,input().split()))

# for i in range(len(num)):
#     k = (i // 3) + 1
#     heap.append(num[i])
#     v = np.sort(heap, kind='heap sort')
#     sum += v[k-1]

# print(sum)
				
				
				
				
				
				
				


# from multiprocessing import Process, Pool

# import heapq
# from heapq import heappush, heappop

# heap = []
# sum = 0

# nums = list(map(int,input().split()))#[7, 6, 5, 4, 3, 2, 1]

# def calcu(findKey):
# 	data = nums[0:findKey+1].copy()
# 	# print(len(data))
# 	k = (findKey // 3) + 1
# 	heapq.heapify(data)
# 	p = heapq.nsmallest(k, data)
# 	# print(k, p[-1])
# 	return p[-1]

# def main():
# 	num_cores = 16
# 	pool = Pool(num_cores)
	
# 	result = pool.map(calcu, range(0, len(nums)))
	
# 	sum = 0
	
# 	for i in range(len(result)):
# 		sum += result[i]
		
# 	print(sum)
# if __name__ == "__main__":
	
# 	main()

#from multiprocessing import Process, Queue
#import time
#import heapq
#from heapq import heappush, heappop


#heap = []

#nums = [7, 6, 5, 4, 3, 2, 1]

#nums = list(map(int,input().split()))#[7, 6, 5, 4, 3, 2, 1]

#def calcu(findKey, saver):
	#g#lobal sum
	#data = nums[0:findKey+1].copy()
	# print(len(data))
	#k = (findKey // 3) + 1
	#h#eapq.heapify(data)
	
	
	#p = heapq.nsmallest(k, data)
	#saver.put(p[-1])
	#print(saver)
	
#def main():
	#result = Queue()
	#for i in range(len(nums)):
		#proc = Process(target=calcu, args=(i, result))
		#proc.start()
		
	#x = 0
	#time.sleep(0.1)
	
#	while True:
#		if result.qsize()== len(nums):
#			while True:
#				x += result.get()
#				if result.empty():
#					print(x)
#					return


#if __name__ == "__main__":
#	main()
"""











