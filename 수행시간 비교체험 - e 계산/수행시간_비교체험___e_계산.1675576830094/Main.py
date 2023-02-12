import time, random

def compute_e_ver1(n):
	if n==0:
			result_final = 1
	else:
		result_final = 1
		for i in range(1,n+1):
			result = 1
			for j in range(1,i+1):
				result*=j
			result_final = result_final + 1/result
		return result_final
	# code for O(n^2)-time version

	
def compute_e_ver2(n):
	if n==0:
		return 1
	else:
		result = 1
		for i in range(1,n+1):
			result*=i
		return compute_e_ver2(n-1)+1/result
	# code for O(n)-time version
	
# n 입력받음
# compute_e_ver1 호출
# compute_e_ver2 호출
# 두 함수의 수행시간 
n = int(input())


#compute_e_ver1 수행시간
before1 = time.process_time()
compute_e_ver1(n)
after1 = time.process_time()
print(after1-before1)

#compute_e_ver2 수행시간 
before2 = time.process_time()
compute_e_ver2(n)
after2 = time.process_time()
print(after2-before2)
