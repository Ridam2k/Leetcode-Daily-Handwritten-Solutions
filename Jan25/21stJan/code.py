from typing import List
import sys

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])
        prefixSum1 = [0 for _ in range(n)]
        prefixSum2 = [0 for _ in range(n)]

        prefixSum1[0] = grid[0][0]
        prefixSum2[0] = grid[1][0]

        for i in range(1, n):
            prefixSum1[i]= prefixSum1[i-1] + grid[0][i]
            prefixSum2[i]= prefixSum2[i-1] + grid[1][i]

        minPts = sys.maxsize
        for i in range(n):
            top = prefixSum1[-1] - prefixSum1[i]
            bottom = prefixSum2[i-1] if i>0 else 0
            secondRobotMax = max(top, bottom)
            minPts = min(minPts,secondRobotMax) 

        return minPts       