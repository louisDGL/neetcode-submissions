class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = 0
        right = n - 1

        while left < right:
            middle = (right - left)//2 + left
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
        
        return nums[left]