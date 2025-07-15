import numpy as np
from typing import List, Tuple

from fe1D.base_element import Base_element

class Mesh1D:    
    def __init__(
        self, 
        x_start: float, 
        x_end: float, 
        min_h: float,
        max_h: float,
        well_x: float, 
        element_type: Base_element,
        N: int = 10, 
        mesh_type: str = 'ordinary'
    ) -> None:
        # TODO: Fix for another elements type
        if element_type.num_nodes() != 2:
            raise TypeError("Mesh generation realized for linear elements only")
            
        self.x_start   = x_start
        self.x_end     = x_end
        self.min_h     = min_h
        self.max_h     = max_h
        self.well_x    = well_x
        self.element   = element_type
        self.N         = N
        self.mesh_type = mesh_type
        
        
        # generate ordinary mesh
        self.generate_mesh()
        
        # find well node
        self.well_nId = self.find_well_node_id() 
        
    def generate_mesh(self):
        if(self.mesh_type == "ordinary"):
            self.generate_ordinary_nodes()
            self.generate_ordinary_elements()
        elif(self.mesh_type == "exponential"):
            self.generate_exponential_nodes()
            self.generate_exponential_elements()
        elif(self.mesh_type == "geometric"):
            self.generate_geometric_nodes()
            self.generate_geometric_elements()
        else:
            raise NameError("Unknown mesh type error")
        
    # Ordinary mesh
    def generate_ordinary_nodes(self) -> None:
        self.nodes = np.linspace(self.x_start, self.x_end, self.N)
    
    def generate_ordinary_elements(self) -> None:
        self.elements = [[i, i + 1] for i in range(self.N)]
        
    # FIXME: Exponential mesh 
    def generate_exponential_nodes(self) -> None:
        xi = np.linspace(0, 1, self.N)
    
        # Divide area by left and right side
        L = self.well_x - self.x_start
        R = self.x_end - self.well_x
        
        left  = self.x_start + L * (np.exp(self.alpha * xi[xi <= 0.5])) / (np.exp(self.alpha))
        right = self.well_x + R * (np.exp(self.alpha * xi[xi > 0.5][::-1])) / (np.exp(self.alpha))
        right = right[::-1]
        
        self.nodes = np.concatenate((left, right))
    
    def generate_exponential_elements(self) -> None:
        pass
    
    def generate_geometric_nodes(self) -> None:
        if(np.mod(self.N, 2) != 0):
            self.N += 1
        
        # Divide area by left and right side
        L = self.well_x - self.x_start
        R = self.x_end - self.well_x
        
        alpha_left  = np.power(L / self.min_h, 2 / self.N)
        alpha_right = np.power(R / self.min_h, 2 / self.N)
        
        left_nodes  = [self.well_x - self.min_h * np.power(alpha_left,  i) for i in range(0, int(self.N / 2))]
        right_nodes = [self.well_x + self.min_h * np.power(alpha_right, i) for i in range(0, int(self.N / 2))]
        
        left_nodes = left_nodes[::-1]
        left_nodes.append(self.well_x)
        self.N += 1
        
        self.nodes = np.concatenate((left_nodes, right_nodes))
    
        
    
    def generate_geometric_elements(self) -> None:
        pass
    
    def find_well_node_id(self) -> int:
        return np.where(self.nodes == self.well_x)[0]
    
    @property
    def get_nodes_count(self):
        return self.N
    
    @property
    def get_nodes(self):
        return self.nodes
    
    @property
    def get_elements(self):
        return self.elements
    