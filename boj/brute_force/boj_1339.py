#백준 1339 - 단어 수학

import sys

n = int(sys.stdin.readline())

alphabet_dict = {'A':0, 'B':0, 'C':0, 'D':0, 'E':0, 'F':0, 'G':0, 'H':0, 'I':0, 'J':0, 'K':0, 'L':0, 'M':0, 'N':0, 'O':0, 'P':0, 'Q':0, 'R':0, 'S':0, 'T':0, 'U':0, 'V':0, 'W':0, 'X':0, 'Y':0, 'Z':0}
alphabet_list = []
answer = 0
pocket = []

for _ in range(n):
    alphabet = input()
    pocket.append(alphabet)

for alphabet in pocket:
    for i in range(len(alphabet)):
        num = 10 ** (len(alphabet) - i - 1)
        alphabet_dict[alphabet[i]] += num

for value in alphabet_dict.values():
    if value > 0:
        alphabet_list.append(value)

sorted_list = sorted(alphabet_list, reverse=True)
for i in range(len(sorted_list)):
    answer += sorted_list[i] * (9 - i)

print(answer)


# 코드 설명
# pocket 리스트에는 n개의 입력되는 알파벳이 저장됩니다.
# 각 알파벳을 순회하며, 각 알파벳의 가치를 계산하여 alphabet_dict에 저장합니다.
# alphabet_list는 내림차순으로 정렬합니다.
# 각 알파벳의 가치를 정렬된 알파벳 리스트에서의 위치에 따라 계산하여 answer에 
# 더합니다.

# 시간 복잡도
# 코드의 시간 복잡도는 O(n * m)이며, 여기서 n은 포켓에 있는 알파벳의 수이고 
# m은 알파벳의 최대 길이입니다.

# 공간 복잡도
# 공간 복잡도는 O(1)

