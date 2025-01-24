from typing import List

class Solution:
    def isCycle(self, graph, vis, vertex, safeNodes):
        #Start path exploration
        vis[vertex] = 2

        for edge in graph[vertex]:
            print(edge)

            if vis[edge] == 2:#has been on this path before
                safeNodes[edge] = False 
                return True
            
            if vis[edge] == 0 and self.isCycle(graph, vis, edge, safeNodes):  
                #not explored before and now while exploring we find cycle
                safeNodes[edge] = False 
                return True
        
        vis[vertex] = 1
        return False

        
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        v = len(graph)
        vis = [0 for _ in range(v)]

        safeNodes = [True for _ in range(v)]

        for i in range(v):
            if not vis[i]:
                if self.isCycle(graph, vis, i, safeNodes):
                    safeNodes[i] = False
        
        # print(safeNodes)
        out = [index for index in range(v) if safeNodes[index] == True]
        # print(out)
        return out
        