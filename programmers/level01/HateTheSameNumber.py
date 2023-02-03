# 프로그래머스 Lv1 - 같은 숫자는 싫어
# 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons


def solution(arr):
    answer = []
    for i in arr:
         if answer[-1:] == [i]: continue
         answer.append(i)
    return answer