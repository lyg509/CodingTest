# 프로그래머스 Lv1 - 삼총사
# 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/131705

import itertools
def solution(number):
    answer = 0
    num_combination = [sum(comb) for comb in itertools.combinations(number,3) if sum(comb) == 0]
    answer = len(num_combination)
        
    return answer

#어떤 쌍(pair)를 return 하고 싶을때 combination을 활용하면 쉽게 구할 수 있습니다.  