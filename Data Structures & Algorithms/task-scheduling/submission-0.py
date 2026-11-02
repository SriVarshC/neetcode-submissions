import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-freq for freq in count.values()]
        heapq.heapify(max_heap)

        cooldown = deque()
        time = 0

        while max_heap or cooldown:
            time += 1

            while cooldown and cooldown[0][1]<= time:
                remaining,available_time = cooldown.popleft()
                heapq.heappush(max_heap,remaining)

            if max_heap:
                remaining = heapq.heappop(max_heap)
                remaining +=1

                if remaining < 0:
                    cooldown.append((remaining,time + n + 1))

        return time

        