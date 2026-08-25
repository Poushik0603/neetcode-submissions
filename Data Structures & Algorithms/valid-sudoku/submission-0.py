class Solution:
    def isVaildList(self, block: List[List[str]]) -> bool:
        lblock = []

        for b in block:
            lblock.extend(b)

        meow = set()

        for b in lblock:
            if b != ".":
                if b in meow:
                    return False
                else:
                    meow.add(b)

        return True

    def isValidRow(self, block: List[str]) -> bool:
        setblock = set()

        for b in block:
            if b != ".":
                if b in setblock:
                    return False
                else:
                    setblock.add(b)

        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)

        # Check rows
        for b in board:
            if not self.isValidRow(b):
                return False

        # Check columns
        for j in range(n):
            seen = set()

            for i in range(n):
                val = board[i][j]

                if val != ".":
                    if val in seen:
                        return False

                    seen.add(val)

        # Check 3x3 blocks
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):

                blocks = [
                    board[x][j:j+3]
                    for x in range(i, i+3)
                ]

                if not self.isVaildList(blocks):
                    return False

        return True