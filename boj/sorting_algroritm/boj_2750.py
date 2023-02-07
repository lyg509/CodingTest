#백준 2750 - 세 수

A, B, C = map(int, input().split())
numbers = [A, B, C]
numbers.sort(reverse=True)
print(numbers[1])
