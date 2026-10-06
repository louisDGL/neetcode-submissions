class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longestLength = 0
        
        for num in nums:
            if num - 1 not in seen:
                currLength = 0
                while num + currLength in seen:
                    currLength += 1
                longestLength = max(longestLength, currLength)
            
        return longestLength