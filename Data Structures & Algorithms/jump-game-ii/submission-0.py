class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        def dfs(i):
            if i == n - 1:
                return 0
            if i in dp:
                return dp[i]
            
            max_step = min(i + nums[i], n - 1)
            res = 100000
            for j in range(i+1,max_step+1):
                res = min(res, 1 + dfs(j))
            dp[i] = res
            return dp[i]
        return dfs(0)