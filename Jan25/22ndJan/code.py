import queue
from typing import List

class Solution:
    def highestPeak(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])

        q = queue.Queue()

        vis = [[False for _ in range(m)] for _ in range(n)]
        ans = [[-1 for _ in range(m)] for _ in range(n)]

        dirX = [0,0,1,-1]
        dirY = [1,-1,0,0]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.put((0, i, j))
                    vis[i][j] = True
                    ans[i][j] = 0
        
        while(not q.empty()):
            curr_val, x, y = q.get()
            # if ans[x][y]!=-1:
            #     ans[x][y] = curr_val

            for i in range(4):
                xx = x + dirX[i]
                yy = y + dirY[i]

                if xx <0 or xx>=n or yy<0 or yy>=m or vis[xx][yy]:
                    continue
                
                q.put((curr_val+1, xx, yy))
                ans[xx][yy] = curr_val + 1
                vis[xx][yy] = True

        return ans    
        