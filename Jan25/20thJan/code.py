from typing import List
import sys

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        lookup = {}

        for i in range(len(arr)):
            lookup[arr[i]] = i

        min_row_idx = sys.maxsize
        min_col_idx = sys.maxsize

        n = len(mat)
        m = len(mat[0])

        for i in range(n):
            greatest_idx = -sys.maxsize
            for j in range(m):
                index = lookup[mat[i][j]]
                greatest_idx = max(index, greatest_idx)
        
            min_row_idx = min(min_row_idx, greatest_idx)
        
        for j in range(m):
            greatest_idx = -sys.maxsize
            for i in range(n):
                index = lookup[mat[i][j]]
                greatest_idx = max(index, greatest_idx)
            
            min_col_idx = min(min_col_idx, greatest_idx)
        
        return min(min_col_idx, min_row_idx)




        