#Python
from collections import deque

class Solution:
    def kahnsTopologicalSort(self, arr, indegree, visited, source):
        queue = deque([source])
        last_node = -1

        while queue:
            curr = queue.popleft()
            visited[curr] = True
            last_node = curr

            neighbor = arr[curr]
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0 and not visited[neighbor]:
                queue.append(neighbor)
        
        return arr[last_node]

    def maxDepthBFS(self, adj, orig_visited, n, source, avoid):
        visited = [False] * n
        queue = deque([source])
        visited[source] = True
        visited[avoid] = True

        levels = 0
        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                orig_visited[curr] = True

                for neighbor in adj[curr]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        queue.append(neighbor)
            levels += 1
        return levels

    def bfs(self, arr, visited, source):
        queue = deque([source])
        visited[source] = True

        count = 0
        while queue:
            curr = queue.popleft()

            if not visited[arr[curr]]:
                visited[arr[curr]] = True
                queue.append(arr[curr])
            count += 1
        return count

    def maximumInvitations(self, arr):
        n = len(arr)
        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for i in range(n):
            adj[arr[i]].append(i)
            indegree[arr[i]] += 1

        total_tail_len = 0
        visited = [False] * n
        for i in range(n):
            if indegree[i] == 0 and not visited[i]:
                node = self.kahnsTopologicalSort(arr, indegree, visited, i) #get the cycle start node for the current component
                if arr[arr[node]] == node:  # if cycle len == 2
                    len_tail = self.maxDepthBFS(adj, visited, n, node, arr[node]) - 1
                    total_tail_len += len_tail  #combined tail len in a component
                    visited[node] = False

        two_size_cycles = 0
        max_cycle_size = 0
        for i in range(n):
            if not visited[i]:
                cycle_size = self.bfs(arr, visited, i) #for getting cycle sizes > 2
                if cycle_size == 2:
                    two_size_cycles += 1
                else:
                    max_cycle_size = max(max_cycle_size, cycle_size) #num of nodes in an arbitrary cycle

        cycle_size_2 = total_tail_len + 2 * two_size_cycles  #number of nodes in cycle size of len 2
        return max(cycle_size_2, max_cycle_size)