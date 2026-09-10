class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        i = 0
        cars = [(position, (target - position) / speed)for position, speed in zip(position, speed)]
        cars.sort(reverse=True)
        
        stack = []
        for c in cars:
            if not stack or stack[-1][1] < c[1]:
                stack.append(c)

        return len(stack)

            
        