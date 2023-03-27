class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        cur_row = [1]
        prev_row = self.getRow(rowIndex-1)
        
        for i in range(1, rowIndex):
            cur_row.append(prev_row[i]+prev_row[i-1])
            
        cur_row.append(1)
        
        return cur_row
        