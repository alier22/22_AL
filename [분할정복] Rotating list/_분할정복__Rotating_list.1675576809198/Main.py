#수행시간
# T(n) = T(n)+c
# T(1) = c
# O(n)

nums = list(map(int, input().split())) #리스트 입력


def find(nums):
	if nums[0] < nums[-1]:#k=0인 경우 회전이 없다
		return len(nums) #len(nums)-find(nums) = 0이 되야하기 때문에 len(nums)출력
	for i in range(1, len(nums)): #1부터 len(nums)까지
		if nums[i] < nums[i-1]: #nums[i]가 nums[i-1]보다 작을 때
			return i #return i
		

print(len(nums) - find(nums))#결과 값



