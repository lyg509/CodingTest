#백준 15819 - 너의 핸들은

N, I = map(int, input().split())
handles = [input() for i in range(N)]

handles.sort()

print(handles[I - 1])


#배열을 sort()를 통해 정렬한 후, I-1 번째 인덱스의 값을 출력합니다