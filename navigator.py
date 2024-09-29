from maze import *
from exception import *
from stack import *
class PacMan:
    navigator_maze = []
    def __init__(self, grid : Maze) -> None:
        self.navigator_maze = grid.grid_representation
    def find_path(self, start, end):
        # IMPLEMENT FUNCTION HERE
        grid=self.navigator_maze
        ROWS, COLS = len(grid), len(grid[0])
        startx=start[0]
        starty=start[1]
        endx=end[0]
        endy=end[1]
        visit = set()
        s=Stack()
        ans=([[[0] for i in range(COLS)] for j in range(ROWS)])
        
        def addCell(r, c):
            if (
                min(r, c) < 0
                or r == ROWS
                or c == COLS
                or (r, c) in visit
                or grid[r][c]==1
            ):
                return
            visit.add((r, c))
            s.push([r, c])
            u=ans[r-dr][c-dc].copy()
            u.append((r,c))
            ans[r][c]=u
            
        
        s.push([endx, endy])
        visit.add((endx, endy))
        ans[endx][endy]=[(endx,endy)]
        
        while not s.is_empty():
            for i in range(s.length()):
                r, c = s.pop()
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in directions:
                    addCell(r + dr, c + dc)
        res=ans[startx][starty][::-1]
        if res==[0] or grid[endx][endy]==1:
            raise PathNotFoundException
        else:
            return res