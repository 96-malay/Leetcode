import collections


class Solution:
    def numIslands(self, grid) -> int:

        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            q = collections.deque()
            q.append((r, c))
            visited.add((r, c))

            while q:
                rc, cc = q.popleft()
                # To check in all 4 given directions
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

                # Checking for adj. land in all 4 directions
                for rd, cd in directions:
                    r = rd+rc
                    c = cd+cc
                    if (r in range(rows) and
                        c in range(cols) and
                        (r, c) not in visited and
                            grid[r][c] == '1'):
                        q.append((r, c))
                        visited.add((r, c))  # Marking this point as visited

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    dfs(r, c)
                    islands += 1
        return islands
