# H)백준 2470
# https://www.acmicpc.net/problem/2470

#문제
#KOI 부설 과학연구소에서는 많은 종류의 산성 용액과 알칼리성 용액을 보유하고 있다. 각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어져있다.  산성 용액의 특성값은 1부터 1,000,000,000까지의 양의 정수로 나타내고, 알칼리성 용액의 특성값은 -1부터 -1,000,000,000까지의 음의 정수로 나타낸다.

#같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의한다. 이 연구소에서는 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들려고 한다. 
#예를 들어, 주어진 용액들의 특성값이 [-2, 4, -99, -1, 98]인 경우에는 특성값이 -99인 용액과 특성값이 98인 용액을 혼합하면 특성값이 -1인 용액을 만들 수 있고, 이 용액이 특성값이 0에 가장 가까운 용액이다. 참고로, 두 종류의 알칼리성 용액만으로나 혹은 두 종류의 산성 용액만으로 특성값이 0에 가장 가까운 혼합 용액을 만드는 경우도 존재할 수 있다.
#산성 용액과 알칼리성 용액의 특성값이 주어졌을 때, 이 중 두 개의 서로 다른 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액을 찾는 프로그램을 작성하시오.
#입력
#첫째 줄에는 전체 용액의 수 N이 입력된다. N은 2 이상 100,000 이하이다. 둘째 줄에는 용액의 특성값을 나타내는 N개의 정수가 빈칸을 사이에 두고 주어진다. 이 수들은 모두 -1,000,000,000 이상 1,000,000,000 이하이다. N개의 용액들의 특성값은 모두 다르고, 산성 용액만으로나 알칼리성 용액만으로 입력이 주어지는 경우도 있을 수 있다.

#출력
#첫째 줄에 특성값이 0에 가장 가까운 용액을 만들어내는 두 용액의 특성값을 출력한다. 출력해야 하는 두 용액은 특성값의 오름차순으로 출력한다. 특성값이 0에 가장 가까운 용액을 만들어내는 경우가 두 개 이상일 경우에는 그 중 아무것이나 하나를 출력한다.

n = int(input())
A = list(map(int, input().split()))

# 모든 값을 절댓값으로 바꾸는데 음수는 -1는, 양수는 1을 같이 튜플로 저장
for i in range(len(A)):
    if A[i] < 0 : A[i]= (-A[i],-1)
    else : A[i] = (A[i],1)

# 절댓값 기준 정렬
A.sort()

abs_min = 2*1e9+1 # 실제값 차이를 절댓값으로 표현
real_min = 2*1e9 + 1 # 실제값의 차이
a = b = A[0][0] # 비교할 두 값의 초기화

# 절댓값 배열 전체 돌리기
for i in range(n-1):

    # 절댓값 기준 정렬이므로 옆의 값과 하나씩 비교 -> 절댓값의 차이가 더 작은 경우
    if abs_min >= A[i+1][0] - A[i][0]:
        # 절댓값의 차이가 작은 경우 실제 값을 더해서 비교
        if abs(real_min) > abs(A[i+1][0]*A[i+1][1] + A[i][0]*A[i][1]):
            real_min = A[i+1][0]*A[i+1][1] + A[i][0]*A[i][1] # 실제값 계산
            abs_min = abs(real_min) # 실제값의 절댓값

            a = A[i+1][0]*A[i+1][1]
            b = A[i][0]*A[i][1]

# 오름차순으로 출력
if a > b:print(b, a)
else: print(a,b)    