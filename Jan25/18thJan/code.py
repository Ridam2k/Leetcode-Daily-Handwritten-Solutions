from typing import List
import heapq

class Solution:
    def minCost(self, grid: List[List[int]]):
        n = len(grid)
        m = len(grid[0])
        
        heap = [(0, 0, 0)]
        heapq.heapify(heap)
        
        vis = [[False for _ in range(m)] for _ in range(n)]
        
        dirX = [0,0,1,-1]
        dirY = [1,-1,0,0]
        
        while(heap):
            cost, x, y = heapq.heappop(heap)
            
            if vis[x][y]:
                continue
            
            if x==n-1 and y==m-1:
                return cost
            
            vis[x][y] = True
            
            for i in range(4):
                newX = x + dirX[i]
                newY = y + dirY[i]
                
                if newX<0 or newY<0 or newX>=n or newY>=m:
                    continue
                
                if (i+1) == grid[x][y]:
                    heapq.heappush(heap, (cost, newX, newY))
                else:
                    heapq.heappush(heap, (cost+1, newX, newY))
        
        return -1