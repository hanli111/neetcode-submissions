class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # pair (position, time)
        cars = [(p, (target - p) / s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        res = 0
        curr_time = 0
        for _, time in cars:
            if time > curr_time:
                res += 1
                curr_time = time
        return res