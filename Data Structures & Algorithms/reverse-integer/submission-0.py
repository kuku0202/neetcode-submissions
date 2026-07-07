class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        ans = 0
        while x:
            ans = ans * 10 + x % 10
            x = x // 10
        return ans * sign if ans <= 2 **31 -1 else 0