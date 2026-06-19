class MedianFinder:

    def __init__(self):
        self.maxlist = []
        self.minlist = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxlist, num)

        if self.minlist and -self.minlist[0] > self.maxlist[0]:
            val = heapq.heappop(self.minlist)
            heapq.heappush(self.maxlist, -val)
        
        if len(self.maxlist) > len(self.minlist) + 1:
            val = heapq.heappop(self.maxlist)
            heapq.heappush(self.minlist, -val)

    def findMedian(self) -> float:
        
        if len(self.maxlist) != len(self.minlist):
            return self.maxlist[0]
        else:
            return (self.maxlist[0] - self.minlist[0]) / 2