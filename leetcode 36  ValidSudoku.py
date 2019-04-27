#leetcode 36 medium
#以为要填满，怎么可能是medium
#好多时候python可麻烦了

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict = {}
        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num!='.':
                    if (num+'inrow'+str(i)) in dict: return False
                    else: dict[num+'inrow'+str(i)] = 0
                    if (num+'incol'+str(j)) in dict: return False
                    else: dict[num+'incol'+str(j)] = 0
                    if (num+'inblock'+str(i//3)+str(j//3)) in dict: return False
                    else: dict[num+'inblock'+str(i//3)+str(j//3)] = 0
        return True