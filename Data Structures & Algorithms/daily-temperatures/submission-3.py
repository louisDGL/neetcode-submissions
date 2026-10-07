class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if stack == []:
                stack.append([temperatures[i], i])
                continue
            
            curr = temperatures[i]
            while stack and curr > stack[-1][0]:
                temp, index = stack.pop()
                res[index] = i - index
            stack.append([curr, i])

        return res