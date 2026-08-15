class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        visited = set()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        
        def addCell(r, c):
            if (min(r, c) >= 0 and r < ROWS and c < COLS and (r, c) not in visited and grid[r][c] != -1):
                visited.add((r, c))
                q.append([r, c])
        
        dist = 0
        while q:
            for i in range (len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell (r + 1, c)
                addCell (r - 1, c)
                addCell (r, c + 1)
                addCell (r, c - 1)
            dist += 1
