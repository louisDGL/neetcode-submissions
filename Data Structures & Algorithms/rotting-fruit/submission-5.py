class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        EMPTY, FRESH, ROTTEN = 0, 1, 2

        q = deque()
        visited = set()

        for r in range (ROWS):
            for c in range(COLS):
                if grid[r][c] == ROTTEN:
                    q.append ([r, c])
                    visited.add((r, c))

        def addCell (r, c):
            if min (r, c) >= 0 and r < ROWS and c < COLS and (r, c) not in visited and grid[r][c] == FRESH:
                visited.add((r, c))
                q.append([r, c])
        
        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
        
        for r in range (ROWS):
            for c in range(COLS):
                if grid[r][c] == FRESH and (r, c) not in visited:
                    return -1

        if len (visited) == 0:
            return 0
        
        return dist - 1