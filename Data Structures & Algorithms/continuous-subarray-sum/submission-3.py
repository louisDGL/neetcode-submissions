class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        left = 0
        right = left + 1

        while left < len(nums) - 1:
            right = left + 1
            tSum = nums[left]
            
            while right < len(nums):
                tSum += nums[right]
                if tSum % k == 0:
                    return True
                right += 1
            left += 1

        return False