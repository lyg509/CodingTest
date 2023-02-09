#백준 23278 - 영화 평가
n,l,h=map(int, input().split())
scores=sorted(list(map(int, input().split())))
ans=sum(scores[l:n-h])/(n-l-h)
print(ans)


# 코드 설명
# sum(scores[l:n-h])/(n-l-h)은 l번째부터 n-h번째 까지의 원소들의 합을 n-l-h로 나눈 값으로 계산된 평균을 의미합니다.

# 시간복잡도 
# 리스트를 정렬하는 것은 O(nlogn)의 시간 복잡도를 갖습니다.
# 리스트의 평균을 구하는 것은 O(n)의 시간 복잡도를 갖습니다.

# 공간복잡도
# O(n)
# n은 입력으로 들어오는 점수의 개수입니다.
# 입력으로 들어오는 점수를 저장하기 위해 "scores" 리스트 하나가 사용되며,
# 리스트의 크기는 n이 되기 때문에 공간 복잡도는 O(n)이 됩니다.