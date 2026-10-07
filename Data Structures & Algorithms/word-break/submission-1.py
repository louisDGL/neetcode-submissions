class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = [0] * len(s)


        def dfs (i):
            if i == len(s):
                return True
            
            if memo[i] == 1:
                return False
            
            memo[i] = 1

            result = False

            for word in wordDict:
                lenWord = len(word)

                if word == s[i:i+lenWord]:
                    result = result or dfs (i+lenWord)
            
            return result

        return dfs(0)