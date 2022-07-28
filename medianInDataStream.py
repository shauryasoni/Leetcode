class MedianFinder:
    import heapq

    def __init__(self):
        self.minheap = []
        self.maxheap = []
        heapq.heapify(self.minheap)
        heapq.heapify(self.minheap)

    def addNum(self, num: int) -> None:
        if len(self.minheap) == 0 and len(self.maxheap) == 0 :
            heapq.heappush(self.minheap, num)
            return

        if len(self.minheap) == len(self.maxheap) :
            heapq.heappush(self.minheap, num)
        
            if self.minheap[0] >= -1*self.maxheap[0] :
                return
            else :
                heapq.heappush(self.maxheap, -1*heapq.heappop(self.minheap))
                heapq.heappush(self.minheap, -1* heapq.heappop(self.maxheap))
                return
        else :

            heapq.heappush(self.minheap, num)
            heapq.heappush(self.maxheap, -1* heapq.heappop(self.minheap))
        
    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap) :
            return self.minheap[0]
        else :
            return (self.minheap[0]+ (-1*self.maxheap[0]))/2.0
