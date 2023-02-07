#백준 10989 - 수 정렬하기 3

import sys

n = int(input().strip())
num_list = [0] * 10001

for _ in range(n):
    num_list[int(input().strip())] += 1

for i in range(10001):
    if num_list[i] != 0:
        for j in range(num_list[i]):
            print(i)