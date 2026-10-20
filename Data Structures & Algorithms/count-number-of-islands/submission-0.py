class Solution:

    def foundIsland (self, grid: List[List[str]], x, y):
        if x >= len(grid) or y >= len(grid[0]) or x < 0 or y < 0:
            return
        if grid[x][y] == "0":
            return
        grid[x][y] = "0"
        self.foundIsland(grid, x + 1, y)
        self.foundIsland(grid, x, y + 1)
        self.foundIsland(grid, x - 1, y)
        self.foundIsland(grid, x, y - 1)
        
    
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == "1":
                    res += 1
                    self.foundIsland(grid, x, y)
        
        return res