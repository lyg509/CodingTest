
import bisect

N = int(input().strip())
tickets = list(map(int, input().strip().split()))
tickets.sort()
max_ticket = tickets[-1]

for i in range(1, max_ticket + 1):
    index = bisect.bisect_left(tickets, i)

    if index < len(tickets) and tickets[index] != i:
        print(i)
        break

    if index == len(tickets) - 1:
        print(max_ticket + 1)


#bisection search 알고리즘을 사용
#Bisection search는 정렬된 리스트에서 특정 값의 위치를 찾는 검색 알고리즘
#bisect_left 함수를 사용하여 주어진 리스트 tickets 에서 i 의 위치를 찾습니다.       
#만약 찾은 위치의 티켓 번호가 i와 다르다면, 그 티켓 번호인 i를 출력하고 루프를 빠져나옵니다.
#만약 찾은 위치가 마지막 티켓 번호의 위치이면, max_tickets + 1을 출력합니다.
