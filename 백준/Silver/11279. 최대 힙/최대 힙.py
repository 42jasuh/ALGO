import heapq
import sys
input = sys.stdin.readline

N = int(input())

arr = []

for _ in range(N):
    num = int(input())
    if num == 0 and arr == []:
        print(0)
    elif num == 0:
        print(heapq.heappop(arr)[1])
    else:
        heapq.heappush(arr, (-num, num))
