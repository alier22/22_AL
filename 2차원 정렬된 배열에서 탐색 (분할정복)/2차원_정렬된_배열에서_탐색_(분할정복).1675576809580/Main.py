#수행시간
# T(n) = T(2/n)+T(2/n)+T(2/n)+c
# T(n) = 3T(2/n) +c
# T(1) = c 
# O(logn)

#Code
def search( arr, fromRow, toRow, fromCol, toCol, key):
	
	i = fromRow + (toRow - fromRow)//2
	j = fromCol + (toCol - fromCol)//2
	
	
	if (arr[i][j] == key): # key가 mid에 있을때 (i, j) return
		print ((i , j))
		return
	
	else:
		if (i != toRow or j != fromCol):  #i가 toRow와 일치하지 않거나 j가 fromCol와 일치하지 않을때 
			search(arr, fromRow, i, j, toCol, key)# 재귀


		if (fromRow == toRow and fromCol + 1 == toCol):
			if (arr[fromRow][toCol] == key):# 일치할때 (i, j) return
				print ((fromRow , toCol))
				return
				

		if (arr[i][j] < key): #a[i][j]가 k의 값보다 작을 때 
			if (i + 1 <= toRow):#i를 1 증가 
				search(arr, i + 1, toRow, fromCol, toCol, key)#다시 재귀
				
		else: #a[i][j]가 k의 값보다 클때 
			if (j - 1 >= fromCol):#j한테 -1
				search(arr, fromRow, toRow, fromCol, j - 1, key)#다시 재귀
			
	
	
n ,key = map(int, input().split()) #n,k 입력 --> n*n 리스트 만들기 
arr = [list(map(int, input().split())) for _ in range(n)] #n*n 배열 원소 입력문

data = []
for i in range(len(arr)):
	data += arr[i]
if data.count(key) == 0: #k의 값이 arr에 없다면(-1 ,-1)출력 / 시간 단축에 좋은 모듈이라고 생각합니다.
	print( (-1, -1) )
	
else:
	search(arr, 0, n - 1, 0, n - 1, key)#k의 값이 arr에있다면 (i,j)출력 




#---------------------------------------------------
#1차원 탐색

# def binary_Serch(arr, k, start , end):
# 	if start > end:
# 		return None
	
# 	mid = (start +end) //2
# 	if k == arr[mid]:
# 			return mid
		
# 	elif k < arr[mid]:
# 			return binary_Serch(arr, k, start, mid-1)
# 	else: 
# 			return binary_Serch(arr, k, mid+1, end)


# n ,k = map(int, input().split())
# arr = list(map(int, input().split()))

# result = binary_Serch(arr, k, 0, n-1)

# if result == None:
# 	print("(-1, -1)")
# else:
# 	print(result)
	
#print(binary_Serch(arr,k))

		

#if k not in arr: # 값이 없다면 (-1,-1출력)
#	return (-1,1)
# k값이 존재 (i ,j )출력

#----------------------------------------------------------------------
# def binary_Serch(arr, k, start , end):
	
# 	if start > end:
# 		return None
	
# 	mid = (start + end) //2 #7
# 	midX = mid //n #1
# 	midY = mid % n #3
	
	
# 	print(arr[midX][midY])
	
# 	if k == arr[midX][midY]:
# 		return midX,midY
		
# 	elif k < arr[midX][midY]:
# 		return binary_Serch(arr, k, start, end-1)
		
# 	else: 
# 		return binary_Serch(arr, k, mid-1, end)


# n ,k = map(int, input().split())
# arr = [list(map(int, input().split())) for _ in range(n)]

# result = binary_Serch(arr, k, 0, n*n-1) #start = 0/ end = n-1

# if result == None:
# 	print("(-1, -1)")
	
# else:
# 	print(result)












