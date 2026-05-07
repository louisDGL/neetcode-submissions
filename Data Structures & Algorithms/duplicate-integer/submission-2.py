class Solution:   
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        idx = 1
        n = len (nums)

        while idx < n:
            if nums[idx] == nums[idx - 1]:
                return True
            idx += 1
        
        return False