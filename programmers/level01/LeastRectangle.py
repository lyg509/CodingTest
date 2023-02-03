# 프로그래머스 Lv1 - 최소 직사각형
# 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/86491

def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

#w, h중 큰 값을 모아서 그 중 큰 값과, w, h중 작은 값을 모아서 그 중 큰 값을 곱하면 간단하게 끝납니다.