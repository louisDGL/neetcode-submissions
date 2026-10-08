class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        long = 0
        short = 0

        long = nums[0]
        short = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            tmp = max(long + nums[i], short)
            long = short
            short = tmp

        return tmp