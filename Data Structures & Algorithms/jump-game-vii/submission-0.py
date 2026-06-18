class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque()
        q.append(0)
        farthest = 0
        while q:
            i = q.popleft()
            if i == len(s) - 1:
                return True
            start = max(i + minJump, farthest + 1)
            for j in range(start, min(i + maxJump + 1, len(s))):
                if s[j] == '0':
                    q.append(j)
            farthest = max(farthest, i + maxJump)
        return False