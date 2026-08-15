class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        preMap = {i:[] for i in range (n)}
        for n1, n2 in edges:
            preMap[n1].append(n2)
            preMap[n2].append(n1)
        
        visited = set()
        count = 0

        def dfs(curr, prev):
            if curr in visited:
                return None
            visited.add(curr)
            for nei in preMap[curr]:
                if nei == prev:
                    continue
                dfs(nei, curr)
            return None


        for i in range (n):
            if i in visited:
                continue
            # Else
            count += 1
            dfs(i, -1)
        
        return count