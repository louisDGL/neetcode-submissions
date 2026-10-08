class Solution:
    def rob(self, nums: List[int]) -> int:
        long = 0
        short = 0

        for i in range(len(nums)):
            tmp = max(long + nums[i], short)
            long = short
            short = tmp

        return tmp