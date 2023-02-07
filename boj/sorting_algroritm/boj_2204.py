#백준 2204 - 도비의 난독증 테스트

while True:
    n = int(input())
    if n == 0:
        break
    sList = []
    for _ in range(n):
        s = input().rstrip()
        sList.append([s.lower(), s])
    sList.sort()
    print(sList[0][1])

# sList 리스트에 각 단어를 저장할 때, 단어를 소문자로 변환한 뒤에 저장하고 
# (s.lower()) 같이 저장된 단어의 원래 형식 (s)도 같이 저장합니다.
# sList를 소문자 기준으로 정렬합니다. (sList.sort())
# sList의 첫 번째 원소의 두 번째 요소 (원래 형식의 단어)를 출력합니다.
# print(sList[0][1])     