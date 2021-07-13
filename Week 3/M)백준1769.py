# M)백준1769 3의 배수
# https://www.acmicpc.net/problem/1769
# 문제
# 문제 1. "양의 정수 X는 3의 배수인가?"
# 
# 이 문제를 아래와 같이 변환하는데, X의 각 자리의 수를 단순히 더한 수 Y를 만든다. 예를 들어 X가 1107이었다면, Y는 1+1+0+7=9가 된다. 그리고 Y에 대해서, 아래와 같은 문제를 생각한다.
# 
# 문제 2. "Y는 3의 배수인가?"
# 큰 수 X가 주어졌을 때, 앞에서 설명한 문제 변환의 과정을 몇 번 거쳐야 Y가 한 자리 수가 되어, X가 3의 배수인지 아닌지를 알 수 있게 될지를 구하는 프로그램을 작성하시오.
# 
# 입력
# 첫째 줄에 큰 자연수 X가 주어진다. X는 1,000,000자리 이하의 수이다.
# 
# 출력  
# 첫째 줄에 문제 변환의 과정을 몇 번 거쳤는지를 출력한다. 이 수는 음이 아닌 정수가 되어야 한다. 둘째 줄에는 주어진 수가 3의 배수이면 YES, 아니면 NO를 출력한다.
def func(num,x):
    if len(num)> 1:
        a = 0
        for i in num:
            a += int(i)
        x += 1
        func(str(a),x)
    else:       
        print(x)
        if int(num) % 3 == 0:print("YES")
        else:print("NO")
        return
number = input()
func(number,0)

