#백준 2529 - 부등호

num = int(input())
op = input().split()
check = [False] * 10
mn, mx = None, None

def poss(i, j, k):
    return (i > j) if k == '>' else (i < j)

def recu(cnt, s):
    global mx, mn
    if cnt > num:
        mn = s if mn is None else mn
        mx = s
    for i in range(10):
        if not check[i]:
            if cnt == 0 or poss(s[-1], str(i), op[cnt - 1]):
                check[i] = True
                recu(cnt + 1, s + str(i))
                check[i] = False


recu(0,"")
print(mx)
print(mn)


# 코드 설명
# 'poss' 함수는 부등호 조건이 만족할 때만 'True'를 반환합니다.
# 'recu' 함수는 재귀함수입니다. 각 자리에 숫자를 재귀적으로 배치하며,'cnt'가
# 'num' 보다 크면 가장 작은 순열이나 가장 큰 순열을 저장합니다.

# 시간 복잡도
# 시간 복잡도는 O(10^num)입니다. 이는 각 자리에 숫자를 하나씩 배치하며 
# 재귀 함수를 수행하기 때문입니다.

# 공간 복잡도
# 공간 복잡도는 O(n)이며, n은 생성하려는 숫자의 수입니다.