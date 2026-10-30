class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        cols = {}
        boxes = {}

        for r in range(9):
            for c in range(9):

                value = board[r][c]

                if value == ".":
                    continue
                
                box = (r//3,c//3)

                if r not in rows:
                    rows[r] = set()

                if c not in cols:
                    cols[c] = set()

                if box not in boxes:
                    boxes[box] = set()

                if value in rows[r] or value in cols[c] or value in boxes[box]:
                    return False

                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)
        return True