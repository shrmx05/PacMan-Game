class Maze:
    def __init__(self, m: int, n : int) -> None:
        ## DO NOT MODIFY THIS
        ## We initialise the list with all 0s, as initially all cells are vacant
        self.grid_representation = []
        for row in range(m):
            grid_row = []
            for column in range(n):
                grid_row.append(0)
            self.grid_representation.append(grid_row)     
             
    
    def add_ghost(self, x : int, y: int) -> None:
        # IMPLEMENT YOUR FUNCTION HERE
        grid=self.grid_representation 
        if x<=len(grid) and y<=len(grid[0]):
            grid[x][y]=1
        return    

    def remove_ghost(self, x : int, y: int) -> None:
        # IMPLEMENT YOUR FUNCTION HERE
        grid=self.grid_representation 
        if x<=len(grid) and y<=len(grid[0]):
            grid[x][y]=0
        return 
        
    def is_ghost(self, x : int, y: int) -> bool:
        # IMPLEMENT YOUR FUNCTION HERE
        grid=self.grid_representation 
        if x<=len(grid) and y<=len(grid[0]):
            if grid[x][y]==0:
                return False
            else:
                return True
        return    
    def print_grid(self) -> None:
        # IMPLEMENT YOUR FUNCTION HERE
        grid=self.grid_representation 
        for lst in grid:
            print(' '.join(map(str, lst)))
        return