class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        left = 0
        right = n - 1

        while left <= right:
            middle = (right - left) // 2 + left

            if nums[middle] == target:
                return middle
            
            if nums[left] <= nums[middle]:
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            
            else:
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1

        return -1