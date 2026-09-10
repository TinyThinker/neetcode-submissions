class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        i = 0
        cars = [(position, (target - position) / speed)for position, speed in zip(position, speed)]
        cars.sort()
        
        stack = [] # monotonically decreasing
        for c in cars:
            while stack and stack[-1][1] <= c[1]:
                stack.pop()
            stack.append(c)
        return len(stack)
        # fleet_leader = None
        # fleets = 0
        # for c in cars:
        #     if not fleet_leader or fleet_leader[1] < c[1]:
        #         fleet_leader = c
        #         fleets += 1

        # return fleets

            
        