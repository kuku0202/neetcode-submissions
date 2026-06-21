class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        
        l = 0
        r = len(cardPoints) - 1
        res = 0

        dp = {}
        def dfs(l, r, step):
            if step == 0:
                return 0
            if (l, r, step) in dp:
                return dp[(l, r, step)]
            
            left = cardPoints[l] + dfs(l+1, r, step-1)
            right = cardPoints[r] + dfs(l, r - 1, step-1)

            dp[(l, r, step)] = max(left, right)
            return dp[(l, r, step)]

        return dfs(l, r, k)