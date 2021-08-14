# 1로 만들기
# https://www.acmicpc.net/problem/1463

# X = (3*a) * (2*b) + 1*c
# 1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
# 2. X가 2로 나누어 떨어지면, 2로 나눈다.
# 3. 1을 뺀다.

# 다 해봐야됨...
# 6의 배수인 경우 -> 1,2,3 전부 할 수 있음
# 3의 배수인 경우 -> 1,3할 수 있음
# 2의 배수인 경우 -> 2,3할 수 있음
# 2,3배수 아닌 경우 -> 1할 수 있음

def num_1(list,a):
    if 1 in list[-1]:
        print(a)
        return
    else:
        s1= set();s2=set();s3=set();s4=set()
        b = set()
        for i in list[-1]:
            if i % 6 == 0: s1 = set([i//3,i//2,i-1])
            elif i % 3 == 0 and i % 2 != 0:s2= set([i//3,i-1])
            elif i % 2 == 0 and i % 3 != 0:s3= set([i//2,i-1])
            elif i %2 != 0 and i %3 != 0:s4= set([i-1])
            b.update(s1 | s2 | s3 | s4) 
        list.append(b)
        a += 1
        num_1(list,a)

n = int(input())
a = 0
num_1([{n}],a)