class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            num = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            if num + nums[i+1] + nums[i+2] > 0:
                break
            if num + nums[-2] + nums[-1] < 0:
                continue
            while j < k:
                val = num + nums[j] + nums[k]
                if val > 0:
                    k -= 1
                elif val < 0:
                    j += 1
                else:
                    res.append([num, nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    k -= 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
        return res