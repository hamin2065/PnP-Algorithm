# 백준10829 이진수 변환
# https://www.acmicpc.net/problem/10829

# 문제
# 자연수 N이 주어진다. N을 이진수로 바꿔서 출력하는 프로그램을 작성하시오.
# 
# 입력
# 첫째 줄에 자연수 N이 주어진다. (1 ≤ N ≤ 100,000,000,000,000)
# 
# 출력
# N을 이진수로 바꿔서 출력한다. 이진수는 0으로 시작하면 안 된다.

def func(n):
    if n == 1: return str(1)
    else: return func(n//2) + str(n%2)

n = int(input())

print(func(n))