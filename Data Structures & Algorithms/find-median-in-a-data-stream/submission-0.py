import heapq

class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)
        largest = -heapq.heappop(self.small)
        heapq.heappush(self.large,largest)

        if len(self.large)> len(self.small):
            smallest = heapq.heappop(self.large)
            heapq.heappush(self.small,-smallest)
        

    def findMedian(self) -> float:
        if len(self.small)> len(self.large):
            return -self.small[0]

        return (-self.small[0] + self.large[0])/2
        
        