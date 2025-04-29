import numpy as np

class Mesh1D:
    a: float = 0
    b: float = 1
    N: int   = 10
    
    well_x: float = 0.5
    
    def __init__(self, a: float, b: float, N: int, well_x: float) -> None:
        self.a      = a
        self.b      = b
        self.N      = N
        self.well_x = well_x
        
    def build_mesh(self) -> np.array:
        return np.linspace(self.a, self.b, self.N)
    
    
     