class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        time, fresh = 0, 0
        q = collections.deque()

        def rotTheFruit(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0 or (r,c) in visited):
                return
            q.append((r,c))
            visited.add((r,c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
        print(fresh)
        time = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = 2
                fresh -= 1
                rotTheFruit(r+1, c)
                rotTheFruit(r-1, c)
                rotTheFruit(r, c+1)
                rotTheFruit(r, c-1)
            time += 1
        print(grid)
        return time if fresh == 0 else -1
