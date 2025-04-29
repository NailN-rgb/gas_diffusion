import numpy as np
from typing import List, Tuple

from ..fe1D.base_element import Base_element

class Mesh1D:
    def __init__(self, start: float, end: float, N: int, well_x: float, element: Base_element) -> None:
        # TODO: Fix for another elements type
        if element.num_nodes() != 2:
            raise TypeError("Mesh generation realized for linear elements only")
            
        self._x_start = start
        self._x_end   = end
        self._N       = N
        self._well_x  = well_x
        self._element = element
        
    def generate_nodes(self) -> List[float]:
        self.nodes = [self.x_start + i * (self.x_end - self.x_start) / self.N for i in range(self.N + 1)]
    
    def generate_elements(self) -> List[List[int]]:
        self.elements = [[i, i + 1] for i in range(self.N)]
        
    def build_mesh(self) -> Tuple[List[float], List[List[int]]]:
        self.generate_nodes()
        self.generate_elements()
    
    @property
    def get_nodes_count(self):
        return self.N
    
    @property
    def get_nodes(self):
        return self.nodes
    
    @property
    def get_elements(self):
        return self.elements
    