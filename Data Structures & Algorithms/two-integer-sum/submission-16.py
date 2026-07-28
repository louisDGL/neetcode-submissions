class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = {}

        for i in range(len(nums)):
            residu = target - nums[i]
            if residu in record:
                return [record [residu], i]
            record[nums[i]] = i
        
        