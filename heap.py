import heapq
heap1 = []
for i in (2,32,545,3,12,6,54):
    heapq.heappush(i,heap1)
    print(heap1[0])
result = heapq.heappop(heap1)