class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereqs[crs].append(pre)
            
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if prereqs[crs] == []:
                return True
            
            visited.add(crs)
            for c in prereqs[crs]:
                if not dfs(c): return False
            visited.remove(crs)
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False

        return True