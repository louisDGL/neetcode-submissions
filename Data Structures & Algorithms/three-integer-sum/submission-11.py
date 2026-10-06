class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        start = 0
        left = start + 1
        right = len(nums) - 1

        while start <= len(nums) - 3:

            while left < right:
                somme = nums[start] + nums[left] + nums[right]
                if somme < 0:
                    left += 1
                elif somme > 0:
                    right -= 1
                elif somme == 0:
                    res.append ([nums[start], nums[left], nums[right]])
                    left += 1
                    while left < len(nums) and nums[left - 1] == nums[left]:
                        left += 1
                    right -= 1
                    while right > 0 and nums[right  + 1] == nums[right]:
                        right -= 1


            start += 1
            while start - 1 >= 0 and start + 1 < len(nums) and nums[start - 1] == nums[start]:
                start += 1

            left = start + 1
            right = len(nums) - 1
    
        return res