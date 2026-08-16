class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        cache = [0] * len(s)

        def dfs (i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if cache[i] != 0:
                return cache[i]
            cache[i] = dfs(i + 1)
            if (i + 1 < n):
                if ((s[i] == "1") or (s[i] == "2" and int(s[i + 1]) < 7)):
                    cache[i] += dfs(i + 2)
            return cache[i]

        return dfs(0)