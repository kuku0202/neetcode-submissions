class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        
        for num in nums:
            if num not in hash_set:
                hash_set.add(num)
            else:
                return False
        return True