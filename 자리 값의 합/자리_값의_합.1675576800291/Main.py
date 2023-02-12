def solve(L, S):
	Dp = [[0], [0]]
	for i in range(1, S+1):
		if i<10:
			Dp[1].append(1)
		else:
			Dp[1].append(0)
	for i in range(2, L+1):
		Dp.append([0])
		for j in range(1, S+1):
			if(j<10):
				Dp[i].append(sum(Dp[i-1][1:j+1]))
			else:
				Dp[i].append(sum(Dp[i-1][j-9:j+1]))
	return Dp[L][S]

L, S = [int(x) for x in input().split()]
print(solve(L, S)%2147483647)

'''
자리수 i == 1이면 1부터 9까지의 경우 값만 존재한다 
그러면 Dp[1][1~9] -> 1 이고 나머지는 0 저장
자리수 i => 2 이상이면 Dp[i][1~9] => sum(Dp[i-1][1~j])
나머지는 sum(Dp[i-1][j-9~j]) 저장 
이처럼 Dp[L]까지 반복하면 Dp[L][S]에는 L자리의 모든 합이 S가 되는 자연수의 개수 저장 

수행시간 분석
'자리수 i => 2 이상이면 Dp[i][1~9] => sum(Dp[i-1][1~j]) 나머지는 sum(Dp[i-1][j-9~j]) 저장' 에서 상수 번의 연산을 L*S번 수행하게 된다. 
점화식을 쓰게 되면  ==> T(n) = O(L*S) -> O(n^2)

'''