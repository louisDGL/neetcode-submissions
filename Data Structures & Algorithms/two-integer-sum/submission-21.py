class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        A = []

        for i, num in enumerate(nums):
            A.append ([num, i])

        A.sort()

        left = 0
        right = len(nums) - 1

        while left < right:
            somme = A[left][0] + A[right][0]
            if somme < target:
                left += 1
            elif somme > target:
                right -= 1
            elif somme == target:
                if A[left][1] < A[right][1]:
                    return [A[left][1], A[right][1]]
                else:
                    return [A[right][1], A[left][1]]
        return False

        