class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9 

        rows = [set() for i in range(N)]
        cols = [set() for i in range(N)]
        boxes = [set() for i in range(N)]

        for r in range(N):
            for c in range(N):

                val = board[r][c]

                if val == '.':
                    continue

                if val in rows[r]:
                    return False
                rows[r].add(val)

                if val in cols[c]:
                    return False
                cols[c].add(val)

                boxIndex = (r // 3)*3 + (c // 3)
                if val in boxes[boxIndex]:
                    return False
                boxes[boxIndex].add(val)

        return True
