class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        pref = 1
        count = 0
        for num in nums:
            pref *= num
            if (count + 1) < len(nums):
                res[count + 1] *= pref
            count += 1
        
        suff = 1
        count = len(res) - 1
        for num in nums[::-1]:
            suff *= num
            if (count - 1) >= 0:
                res[count - 1] *= suff
            count -= 1

        return res