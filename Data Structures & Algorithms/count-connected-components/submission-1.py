class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = [False] * n
        for e1, e2 in edges:
            graph[e1].append(e2)
            graph[e2].append(e1)
        def dfs(e):
            for edge in graph[e]:
                if not visited[edge]:
                    visited[edge] = True
                    dfs(edge)

        res = 0
        for e in range(n):
            if not visited[e]:
                visited[e] = True
                dfs(e)
                res += 1
        return res