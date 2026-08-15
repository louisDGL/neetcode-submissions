class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i: [] for i in range (numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visiting = set()

        res = []

        def dfs(crs):
            if crs in visiting:
                # Cycle detected
                return False
            
            if preMap[crs] == []:
                # All prerequisites done
                if crs not in res:
                    res.append (crs)
                return True

            visiting.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre):
                    return False
            visiting.remove(crs)
            preMap[crs] = []
            if crs not in res:
                res.append(crs)
            return True

        
        for c in range (numCourses):
            if not dfs(c):
                return []
        
        return res