from collections import deque

# BFS approach


class Solution:
    def isBipartite(self, graph) -> bool:

        levelOrder = [-1] * len(graph)
        visited = [-1] * len(graph)

        def bfs(root):
            q = deque()
            q.append(root)
            visited[root] = 1
            levelOrder[root] = 0
            while q:
                node = q.popleft()
                for neighbour in graph[node]:
                    if visited[neighbour] == -1:
                        visited[neighbour] = 1
                        levelOrder[neighbour] = 1 + levelOrder[node]
                        q.append(neighbour)
                    else:
                        # if it is same level cross edge
                        if levelOrder[neighbour] == levelOrder[node]:
                            return False
            return True

        for v in range(len(graph)):
            if visited[v] == -1:
                if bfs(v) == False:
                    return False
        return True


# DFS


class Solution:
    def isBipartite(self, graph) -> bool:

        levelColor = [-1] * len(graph)
        visited = [-1] * len(graph)

        def dfs(root):
            visited[root] = 1
            for neighbour in graph[root]:
                if visited[neighbour] == -1:
                    visited[neighbour] = 1
                    levelColor[neighbour] = not levelColor[root]
                    if dfs(neighbour) == False:
                        return False
                else:
                    # back edge with same color
                    if levelColor[neighbour] == levelColor[root]:
                        return False
            return True

        for v in range(len(graph)):
            if visited[v] == -1:
                levelColor[v] = 0
                if dfs(v) == False:
                    return False
        return True
