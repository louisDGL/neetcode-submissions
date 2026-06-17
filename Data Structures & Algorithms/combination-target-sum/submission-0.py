class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        seen = set()

        def dfs (i, subset):
            if sum(subset) == target and ''.join(str(sub) for sub in subset) not in seen:
                res.append(subset.copy())
                seen.add(''.join(str(sub) for sub in subset))
                return
            if sum(subset) > target:
                return
            if i >= len(nums):
                return 
            subset.append (nums[i])
            dfs(i, subset)
            dfs(i+1, subset)
            subset.pop()
            dfs(i+1, subset)

        dfs(0, [])

        return res