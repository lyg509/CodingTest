# 프로그래머스 Lv1 - 최대공약수와 최소공배수
# 문제링크: https://programmers.co.kr/learn/courses/30/lessons/12940

import math
def solution(n, m):
    answer = []
    # 최대공약수
    # 최대공약수는 n과 m중 min을 이용해서 최소값을 구하고 
    # 최소값부터 0까지 for문을 이용해서 n%i==0과 m%i==0이 참이면
    # append를 이용해서 answer 리스트에 i를 넣어준다.
    for i in range(min(n,m),0,-1): 
        if n%i ==0 and m%i==0:
            answer.append(i)
            break

    # 최소공배수
    # 최소공배수는 n과 m중 max를 이용해서 최대값을 구하고 
    # 최대값부터 n*m까지 for문을 이용해서 i%n ==0과 i%m==0이
    # 참이면 append를 이용해서 answer 리스트에 i를 넣어준다.
    for i in range(max(n,m),n*m+1):
        if i%n == 0 and i%m == 0:
            answer.append(i)
            break
    return answer