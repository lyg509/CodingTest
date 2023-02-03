# 프로그래머스 Lv1 - 이상한 문자 만들기
# 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/12930


def solution(s):
    answer = ''
    new_list = s.split(' ')
    for i in new_list:
        for j in range(len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= ' '
    return answer[0:-1]