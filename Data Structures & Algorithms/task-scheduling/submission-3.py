class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        mp = Counter(tasks)
        max_freq = max(mp.values())
        idle_spots = (max_freq - 1) * n

        for freq in mp.values():            
            # decrement number of idle spots from the tasks
            idle_spots -= min(freq, max_freq - 1)
        
        # add back max frequency - 1
        idle_spots += max_freq - 1
        
        return len(tasks) + max(0, idle_spots)