# this is an example of topological sort
# if it's cycle it is not possible to take any course
# in directed graph DFS when it's back edge detect it's departure time always not set

class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        adjlist = [[] for _ in range(numCourses)]

        for src, dest in prerequisites:
            adjlist[dest].append(src)

        visited = [-1] * numCourses
        arrival = [-1] * numCourses
        departure = [-1] * numCourses
        timeStamp = [0]

        def dfs(root):
            visited[root] = 1
            timeStamp[0] += 1
            arrival[root] = timeStamp[0]
            for neighbour in adjlist[root]:
                if visited[neighbour] == -1:
                    if dfs(neighbour):
                        return True
                else:
                    # cycle found back edge
                    if departure[neighbour] == -1:
                        return True
            timeStamp[0] += 1
            departure[root] = timeStamp[0]
            return False

        for v in range(numCourses):
            if visited[v] == -1:
                if dfs(v):
                    return False
        return True
