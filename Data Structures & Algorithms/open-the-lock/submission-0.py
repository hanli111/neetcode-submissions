class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" == target: return 0

        visited = set(deadends)
        if "0000" in visited: return -1

        q = deque(["0000"])
        visited.add("0000")
        turns = 0
        while q:
            turns += 1
            for _ in range(len(q)):
                lock = q.popleft()
                for i in range(4):
                    for j in (-1, 1):
                        digit = str((int(lock[i]) + j + 10) % 10)
                        next_lock = lock[:i] + digit + lock[i + 1:]
                        if next_lock in visited: continue
                        if next_lock == target: return turns
                        q.append(next_lock)
                        visited.add(next_lock)
        return -1