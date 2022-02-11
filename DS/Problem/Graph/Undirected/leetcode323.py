from collections import deque
from collections import defaultdict, deque

# using BFS and adjacency maps


class Solution:
    def countComponents(self, n: int, edges) -> int:
        adjust = defaultdict(list)
        visited = defaultdict(int)
        count = 0
        for (src, des) in edges:
            adjust[src].append(des)
            adjust[des].append(src)
        print(adjust.keys())

        def bfs(node):
            q = deque()
            q.append(node)
            visited[node] = 1
            while q:
                node = q.popleft()
                for neighbour in adjust[node]:
                    if not visited[neighbour]:
                        visited[neighbour] = 1
                        q.append(neighbour)
        for v in range(n):
            if not visited[v]:
                count += 1
                bfs(v)
        return count

# using dfs and adjacency list


class Solution:
    def countComponents(self, n: int, edges) -> int:
        adjust = [[] for _ in range(n)]
        visited = [-1] * n
        count = 0
        for (src, des) in edges:
            adjust[src].append(des)
            adjust[des].append(src)
        print(adjust)

        def dfs(node):
            visited[node] = 1
            for neighbour in adjust[node]:
                if visited[neighbour] == -1:
                    visited[neighbour] = 1
                    dfs(neighbour)
        for v in range(n):
            if visited[v] == -1:
                count += 1
                dfs(v)
        return count
