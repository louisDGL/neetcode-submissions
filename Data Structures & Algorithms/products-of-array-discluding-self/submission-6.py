class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = []
        suff = []

        for num in nums:
            if len(pref) == 0:
                pref.append(num)
            else:
                pref.append(num * pref[-1])
        for num in nums[::-1]:
            if len(suff) == 0:
                suff.append(num)
            else:
                suff.append(num * suff[-1])
        suff = suff[::-1]

        res = []
        for i in range (len(nums)):
            if i - 1 < 0:
                res.append(suff[i + 1])                
            elif i + 1 >= len(suff):
                res.append(pref[i - 1])
            else:
                res.append(pref[i - 1] * suff[i + 1])

        return res