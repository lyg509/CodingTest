#백준 23968 - 알고리즘 수업 - 버블 정렬 1

def bubble_sort(nums, k):
    count = 0
    answer = -1

    for i in range(n-1, 0, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                count += 1
                nums[j], nums[j+1] = nums[j+1], nums[j]

                if count == k:
                    answer = f'{nums[j]} {nums[j+1]}'	

    return answer

n, k = map(int, input().split())
nums = list(map(int, input().split()))
print(bubble_sort(nums, k))

# 코드 설명
# 정렬 과정에서 숫자가 교환 될 때마다 'count' 값을 1 증가 시킵니다.
# 'count' 값이 'k' 와 같아진다면, 교환된 두 수를 출력합니다.
# 버블 정렬 알고리즘
# 주어진 리스트에서 인접한 두 원소를 비교하여 정렬하는 알고리즘

# 시간 복잡도 
# 시간 복잡도는 O(n^2)입니다.
# 크기 n의 리스트를 정렬하는 과정에서 버블 정렬 알고리즘을 사용하기 때문입니다.
# 버블 정렬은 리스트의 원소 개수 n에 비례하여 n^2번의 비교와 교환 작업을 
# 수행하기 때문입니다. 이에 따라, 리스트의 크기가 커지면 그에 비례하여 수행 
# 시간이 증가합니다.

# 공간 복잡도
# 공간 복잡도는 O(n) 입니다.