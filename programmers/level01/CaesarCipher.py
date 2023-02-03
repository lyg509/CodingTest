# 프로그래머스 Lv1 - 시저 암호
# 문제링크: https://school.programmers.co.kr/learn/courses/30/lessons/12926


def caesar(s, n):
    s = list(s)
    for i in range(len(s)):
        if s[i].isupper():
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return "".join(s)

#chr(), ord() 함수를 이용하여 코드를 작성합니다.
#chr(i)는 아스키(ASCII) 코드 값을 입력받아 그 코드에 해당하는 문자를 
#출력하는 함수,
#>>> chr(97) # 'a'
#ord(c)는 문자의 아스키 코드 값을 돌려주는 함수입니다.
#>>> ord('a') # 97   
