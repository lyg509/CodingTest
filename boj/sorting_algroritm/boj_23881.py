#백준 23881 - 영화 평가

n, k = map(int, input().split())
li = list(map(int, input().split()))
count = 0

for i in range(n - 1, 0, -1):
    idx = li.index(max(li[:i + 1]))
    if idx != i:
        li[idx], li[i] = li[i], li[idx]
        count += 1
        if count == k:
            print(li[idx], li[i])
            exit()
print(-1)

# 코드 설명
# 리스트의 n-1 번째부터 0 번째까지 반복하면서 각 인덱스의 최댓값을 찾습니다.
# 구한 최댓값의 인덱스와 현재 인덱스를 교환합니다.
# 교환 횟수가 k와 같아지면 교환된 두 수를 출력하고 프로그램을 종료합니다.
# 번째 큰 수가 없을 경우, -1을 출력합니다.

# 시간 복잡도
# 시간 복잡도는 O(n^2)입니다.
# 주어진 리스트의 크기 n에 따라, for 루프가 n-1부터 0까지 순회하기 때문에 
# 전체 for 루프는 n-1 + (n-2) + ... + 1 = n(n-1)/2 번의 수행이 필요합니다.
# 각 루프 안에서, max() 함수와 li.index() 함수는 각각 O(n)의 시간 복잡도를 
# 가지고 있으므로, 한 루프의 시간 복잡도는 O(n^2)입니다.

# 공간 복잡도
# 공간 복잡도는 O(n)입니다.

