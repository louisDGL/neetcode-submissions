class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ROWS, COLS = len(board), len(board[0])
        
        def dfs(r, c):
            q = []
            current = []
            visited = set()
            q.append([r, c])
            while q:
                r, c = q.pop()
                if min(r, c) >= 0 and r < ROWS and c < COLS:
                    if board[r][c] == "O" and (r, c) not in visited:
                        q.append ([r + 1, c])
                        q.append ([r - 1, c])
                        q.append ([r, c + 1])
                        q.append ([r, c - 1])
                        current.append([r, c])
                        visited.add((r, c))
                else:
                    return
            for r, c in current:
                board[r][c] = "X"
             

        for r in range (ROWS):
            for c in range (COLS):
                if board[r][c] == "O":
                    dfs(r, c)
                
                