#백준 9076 - 점수 집계

x = int(input())
for i in range(x):
    points = sorted(map(int, input().split()))[1:-1]
    if max(points) - min(points) >= 4:
        print('KIN')
    else:
        print(sum(points))


#[1:-1] 첫 번째 요소와 마지막 요소를 제외하는 데 사용        