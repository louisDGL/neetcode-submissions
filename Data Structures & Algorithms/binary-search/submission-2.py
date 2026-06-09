class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (right - left) // 2 + left
            valueMiddle = nums[middle]
            
            if valueMiddle == target:
                return middle
            if valueMiddle < target:
                left = middle + 1
            elif valueMiddle > target:
                right = middle - 1
        
        return -1