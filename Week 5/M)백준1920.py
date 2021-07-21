# M)백준1920 수 찾기
# https://www.acmicpc.net/problem/1920

# 문제
# N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

# 출력
# M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

n = int(input())
A = list(map(int, input().split()))
m = int(input())

# sort를 해야하는데 출력할 때 원래의 index가 필요하기 때문에 index같이 저장
B = list(enumerate(map(int, input().split())))
C = [0 for _ in range(m)]

A.sort()

# B의 index가 아닌 value로 값 정렬시키기
B.sort(key = lambda x:x[1])

i = 0 # A의 인덱스
j = 0 # B의 인덱스

while i < n and j < m:
    # A와 B에서 같은 숫자가 나오면 B의 원래 인덱스 자리 찾아서 C[]값 바꿔주기
    if A[i] == B[j][1]:
        C[B[j][0]] = 1
        j += 1
    # B리스트에 있는 값이 더 크면 A에서는 못찾았다는 뜻이므로 A index 증가
    elif A[i] < B[j][1] : i += 1
    else : j += 1
for x in range(m):
    print(C[x])
    