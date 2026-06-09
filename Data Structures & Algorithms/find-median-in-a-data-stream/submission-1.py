import heapq

class MedianFinder:
    # What is the median is the middle value of a sorted list.
    # We can achieve this via sorting each time but we'd have an nlogn solution everytime we add or remove.
    # Can we do better? We can have these operations be logn if we use add and remove from heaps.
    # But how? Well if the median is the middle of a sorted list, then we know that we can 
    # split the list in two. The large and the small nums. The largest number of the smallest or the 
    # smallest numbers of the largest or the mean of the two would be the Median.

    def __init__(self):
        self.small, self.large = [], [] #small is a max since we want the biggest of the small numbers. 
                                        #large is a min heap
        

    def addNum(self, num: int) -> None:
        if self.large and num > self.large[0]: # if large not empty and num is greater than the smallest of the large
            heapq.heappush(self.large, num)
        else:
            heapq.heappush(self.small, -1 * num)

        # Do we need to rebalance
        # if not, let's get the hell out of there
        if abs(len(self.small) - len(self.large)) <= 1:
            return 

        if len(self.small) > len(self.large):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        else:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large):
           return (-1 * self.small[0] + self.large[0]) / 2.0
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        return self.large[0]
