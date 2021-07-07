# L)백준2447_별 찍기 - 10
# https://www.acmicpc.net/problem/2447

# 문제
# 재귀적인 패턴으로 별을 찍어 보자. N이 3의 거듭제곱(3, 9, 27, ...)이라고 할 때, 크기 N의 패턴은 N×N 정사각형 모양이다.
# 크기 3의 패턴은 가운데에 공백이 있고, 가운데를 제외한 모든 칸에 별이 하나씩 있는 패턴이다.
# ***
# * *
# ***
# N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진 가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 둘러싼 형태이다. 예를 들어 크기 27의 패턴은 예제 출력 1과 같다.
# 
# 입력
# 첫째 줄에 N이 주어진다. N은 3의 거듭제곱이다. 즉 어떤 정수 k에 대해 N=3k이며, 이때 1 ≤ k < 8이다.
# 
# 출력
# 첫째 줄부터 N번째 줄까지 별을 출력한다.

def star(a,b,n):
	if n == 1: 
		return
	if a > l*l or b > l*l:
		return
	for i in range(3):
		for j in range(3):
			star((a-n//3)+(i*n//3),(b-n//3)+(j*n//3),n//3)
	star_blank(a,b,n)

# n이면 (n/3)*(n/3)크기의 박스를 지워야함
def star_blank(a,b,n):
	m = n//3
	# a와 b의 starting point잡기
	a -= m//2
	b -= m//2
	for i in range(m):
		for j in range(m):
			list[a+i][b+j] = ' '

n = int(input())

list = [["*"for _ in range(n)]for _ in range(n)]
l = len(list)
star(n//2,n//2,n)   


for i in list:
	print(''.join(i))
