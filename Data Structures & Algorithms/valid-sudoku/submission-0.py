class Solution:

    def isValidUnit(self, unit: List[str]) -> bool:
        nums = [num for num in unit if num != "."]
        return len(nums) == len(set(nums))

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValidUnit(board[i]):
                return False
            if not self.isValidUnit([board[j][i] for j in range(9)]):
                return False
        
        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                subBox = [board[i][j] 
                        for i in range(box_row, box_row + 3) 
                        for j in range(box_col, box_col + 3)]

                if not self.isValidUnit(subBox):
                    return False
        return True 