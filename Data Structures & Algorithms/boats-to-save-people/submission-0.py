class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        boats = 0

        while l <= r:
            space_left = limit - people[r]
            boats += 1
            r -= 1
            if l <= r and space_left >= people[l]:
                l += 1
        return boats
            

        '''
        [1, 2, 4, 5]    limit = 6
         L        R
        '''