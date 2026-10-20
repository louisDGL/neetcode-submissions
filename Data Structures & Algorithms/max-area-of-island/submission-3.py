class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        curArea = 0

        deplacements = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def foundIsland(x, y):
            nonlocal curArea
            if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0:
                return
            if grid[x][y] == 0:
                return
            curArea += 1
            grid[x][y] = 0
            for dg, dr in deplacements:
                foundIsland(x + dg, y + dr)
            return


        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    curArea = 0
                    foundIsland(x, y)
                    maxArea = max(maxArea, curArea)
        
        return maxArea