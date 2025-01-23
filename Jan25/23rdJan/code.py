from typing import List

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        rowFreq = [0 for _ in range(n)]
        colFreq = [0 for _ in range(m)]

        n_servers = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rowFreq[i] +=1
                    colFreq[j]+=1
                    n_servers+=1
        
       
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and rowFreq[i]<=1 and colFreq[j]<=1:
                    n_servers-=1
        
        return n_servers

        
