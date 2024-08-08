import threading
from typing import List

class solve:
    def solveProblem(self, n: int) -> List[List[str]]:
        col = set() 
        positiveDiag = set() #row + col
        negativeDiag = set() #row - col

        res = []
        board = [["."] * n for i in range(n)]
        lock = threading.Lock()

        def backTracking(r, col, positiveDiag, negativeDiag, board):
            if r == n:
                copy = ["".join(row) for row in board]
                with lock:
                    res.append(copy)
                return 
            
            for c in range(n):
                if c in col or r + c in positiveDiag or r - c in negativeDiag:
                    continue

                col.add(c)
                positiveDiag.add(r + c)
                negativeDiag.add(r - c)
                board[r][c] = "Q"

                backTracking(r + 1, col, positiveDiag, negativeDiag, board)

                col.remove(c)
                positiveDiag.remove(r + c)
                negativeDiag.remove(r - c)
                board[r][c] = "."
        
        def tableCopies(c):
            newCol = col.copy()
            newPositiveDiag = positiveDiag.copy()
            newNegativeDiag = negativeDiag.copy()
            newBoard = [row[:] for row in board]

            newCol.add(c)
            newPositiveDiag.add(0 + c)
            newNegativeDiag.add(0 - c)
            newBoard[0][c] = "Q"

            backTracking(1, newCol, newPositiveDiag, newNegativeDiag, newBoard)

        threads = []

        for c in range(n):
            t = threading.Thread(target = tableCopies, args=(c,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

        return res
    
sol = solve()
print(sol.solveProblem(4))