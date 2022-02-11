from collections import deque

# using BFS


class Solution:
    def validTree(self, n: int, edges) -> bool:
        adjacency = [[] for _ in range(n)]
        visited = [-1] * n
        parent = [-1] * n

        for src, dest in edges:
            adjacency[src].append(dest)
            adjacency[dest].append(src)
        print(adjacency)

        def bfs(node):
            q = deque()
            q.append(node)
            visited[node] = 1
            while q:
                n = q.popleft()
                for neighbour in adjacency[n]:
                    if visited[neighbour] == -1:
                        visited[neighbour] = 1
                        q.append(neighbour)
                        parent[neighbour] = n
                    else:
                        if neighbour != parent[n]:
                            return True
            return False

        componentCount = 0
        for v in range(n):
            if visited[v] == -1:
                componentCount += 1
                # more than one component means graph is not connected
                if componentCount > 1:
                    return False
                # graph has a cycle so not tree
                if bfs(v):
                    return False
        return True

# DFS approach


class Solution:
    def validTree(self, n: int, edges) -> bool:
        adjacency = [[] for _ in range(n)]
        visited = [-1] * n
        parent = [-1] * n

        for src, dest in edges:
            adjacency[src].append(dest)
            adjacency[dest].append(src)
        print(adjacency)

        def dfs(node):
            visited[node] = 1
            for neighbour in adjacency[node]:
                if visited[neighbour] == -1:
                    visited[neighbour] = 1
                    parent[neighbour] = node
                    if dfs(neighbour):
                        return True
                else:
                    if neighbour != parent[node]:
                        return True

            return False

        componentCount = 0
        for v in range(n):
            if visited[v] == -1:
                componentCount += 1
                if componentCount > 1:
                    return False
                if dfs(v):
                    return False
        return True
