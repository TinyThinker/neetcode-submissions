class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #position [i] - location of car in miles
        #speed[i] - speed of car
        #target = destination in miles

        #cars cannot pass each other
        #this means the largest position car is the limiter of all the rest

        pairs = []
        for i in range(len(position)):
            pairs.append((position[i], speed[i], (target - position[i])/ speed[i]))
        pairs.sort(reverse=True)
        
        fleet = 0
        while pairs:
            print(f"{pairs}")
            fleet += 1
            lead = pairs.pop(0)
            while pairs and pairs[0][2] <= lead[2]:
                pairs.pop(0)
        return fleet

