# L)백준2535 아시아 정보올림피아드
# https://www.acmicpc.net/problem/2535

n = int(input())

# 각 국가별로 높은 점수 2명씩 뽑기
l = []
for i in range(n):
    l.append(tuple(map(int, input().split())))

l.sort(key=lambda x:x[2],reverse=True)

result = []
result.append(l[0])
result.append(l[1])
i = 2
while len(result) != 3:
    if l[i][0] == l[0][0] and l[i][0] == l[1][0]:
        i += 1
    else:
        result.append(l[i])

for k in result:
    print(k[0],k[1])