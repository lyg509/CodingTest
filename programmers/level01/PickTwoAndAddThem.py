# 프로그래머스 Lv1 - 두 개 뽑아서 더하기
# 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/68644

from itertools import combinations
def solution(numbers):
    answer = set()
    for i in list(combinations(numbers,2)):
        answer.add(sum(i))
    return sorted(answer)

#파이썬 기본 라이브러리인 itertools의 combinations 라는 내장함수를 사용하여 인자값에 따라 해당 요소로 구할수 있는 모든 조합을 리턴합니다.