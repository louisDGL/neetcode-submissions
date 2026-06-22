class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
        seen = set()

        rows, cols = len(grid), len(grid[0])

        self.currArea = 0

        def dfs(x, y):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            self.currArea += 1
            seen.add((x, y))
            for dx, dy in directions:
                x2 = x + dx
                y2 = y + dy
                if x2 in range (rows) and y2 in range(cols) and (x2, y2) not in seen and grid[x2][y2] == 1:
                    dfs(x2, y2)

        for x in range(rows):
            for y in range(cols):
                space = grid[x][y]

                if space == 1 and (x, y) not in seen:
                    self.currArea = 0
                    dfs(x, y)
                    maxArea = max(maxArea, self.currArea)
        
        return maxArea