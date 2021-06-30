# M)백준10828_스택
# https://www.acmicpc.net/problem/10828
# 
# 문제
# 정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
# 명령은 총 다섯 가지이다.
# - push X: 정수 X를 스택에 넣는 연산이다.
# - pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# - size: 스택에 들어있는 정수의 개수를 출력한다.
# - empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
# - top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
#
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.
# 
# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

# **시간제한 : 0.5 초 (추가 시간 없음)**

import sys

class Stack:
    def __init__(self):
        self.list = []
        self.num = 0

    def push(self, x):
        self.list.append(x)
        self.num += 1
        return
    def pop(self):
        if self.num == 0:
            return -1
        else:
            self.num -= 1
            return self.list.pop(-1)
    def size(self):
        return self.num

    def empty(self):
        if self.num == 0:
            return 1
        else:
            return 0

    def top(self):
        if self.num == 0:
            return -1   
        else:
            return self.list[-1]

# readline()은 개행문자(줄 바꿈 문자)를 포함.
# input : prompt message를 출력하고, 개행 문자를 삭제한 값을 리턴하기 때문에 느림 -> sys.stdin.readline() 사용
num = int(sys.stdin.readline())
S = Stack()
for i in range(num):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        S.push(cmd[1])
    elif cmd[0] == 'pop':
        print(S.pop())
    elif cmd[0] == 'size':
        print(S.size())
    elif cmd[0] == 'empty':
        print(S.empty())
    elif cmd[0] == 'top':
        print(S.top())
