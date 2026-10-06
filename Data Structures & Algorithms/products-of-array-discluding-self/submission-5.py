class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        fullProd = 1
        zeros = 0
        for num in nums:
            if num == 0:
                zeros += 1
            if num != 0:
                fullProd *= num
        
        final = []
        for num in nums:
            if num == 0 and zeros == 1:
                final.append(fullProd)
            elif num != 0 and zeros == 0:
                final.append(int(fullProd/num))
            else:
                final.append(0)
        return final