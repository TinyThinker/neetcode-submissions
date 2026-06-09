class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = 1
        car = [(p, s) for p, s in zip(position, speed)]
        car.sort(reverse=True)

        prevTime = (target - car[0][0]) / car[0][1]
        for i in range(1, len(car)):
            currTime = (target - car[i][0]) / car[i][1]
            if currTime > prevTime:
                fleets += 1
                prevTime = currTime
        


        return fleets