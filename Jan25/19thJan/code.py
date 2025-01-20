from typing import List
import heapq

class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        n = len(heightMap)
        m = len(heightMap[0])

        pq = []
        heapq.heapify(pq)
        vis= [[False for _ in range(m)] for _ in range(n)]

        minBdHt = 0
        water = 0

        for i in range(n):
            for j in range(m):
                #boundary cells
                if (i == 0 or i == n-1 or j==0 or j == m-1):
                    heapq.heappush( pq, (heightMap[i][j],i,j ) )
                    vis[i][j] = True  #mark visited here
        
        dirX = [0,0,1,-1]
        dirY = [1,-1,0,0]

        while(pq):
            curr  = heapq.heappop(pq)
            currHt = curr[0]
            x = curr[1]
            y = curr[2]
            minBdHt = max(currHt, minBdHt)

            # print(currHt, x, y)

            for i in range(4):
                xx = x + dirX[i]
                yy = y + dirY[i]

                if(xx<0 or xx>=n or yy<0 or yy>= m or vis[xx][yy]):
                    continue

                heapq.heappush(pq, (heightMap[xx][yy], xx, yy) )
                vis[xx][yy] = True      #and mark here so we don't process again

                if(heightMap[xx][yy] < minBdHt):
                    water+= (minBdHt - heightMap[xx][yy])

        return water
        