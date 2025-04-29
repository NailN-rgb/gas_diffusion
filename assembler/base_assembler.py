from abc import ABC, abstractmethod
from typing import List, Tuple
import numpy as np

from equation.base_equation import Equation
from fe1D.base_element import Base_element
from mesh1D.mesh1D import Mesh1D

class BaseAssembler():
    @abstractmethod
    def __init__(self, mesh: Mesh1D, equation: Equation, element: Base_element) -> None:
        self.mesh = mesh
        self.equation = equation
        self.element = element
    
    @abstractmethod
    def assemble_element(self, elem_nodes: List[float]) -> Tuple[List[List[float]], List[List[float]], List[float]]:
        pass
    
    def assemble_global(self) -> None:
        n_nodes = self.mesh.get_nodes_count()
        
        self.M = np.zeros((n_nodes, n_nodes))
        self.K = np.zeros((n_nodes, n_nodes))
        self.F = np.zeros(n_nodes)
        
        mesh_nodes    = self.mesh.get_nodes()
        mesh_elements = self.mesh.get_elements()
        
        for elem_nodes in mesh_elements:
            x_coords = [mesh_nodes[i] for i in range(elem_nodes)]
            local_M, local_K, local_F = self.assemble_element(x_coords)
            
            for i_local, i_global in enumerate(elem_nodes):
                self.F[i_global] += local_F[i_local]
                for j_local, j_global in enumerate(elem_nodes):
                    self.M[i_global, j_global] += local_M[i_local, j_local]
                    self.K[i_global, j_global] += local_K[i_local, j_local]
                    
    # For linear elements only
    def assemble_dirichlet(self, boundary_node: int, value: float):
        self.K[boundary_node, :] = 0.0
        self.K[:, boundary_node] = 0.0
        self.K[boundary_node, boundary_node] = 1.0
        self.F[boundary_node] = value
        
    def assemble_neumann(self, boundary_node: int):
        # Left corner
        if boundary_node == 0:
            dx = self.mesh.get_nodes()[1] - self.mesh.get_nodes()[1]
            dr = self.equation.flow_term(self.mesh.get_nodes()[0] + dx / 2)
            self.K[0, 0] += dr / dx
            self.K[0, 1] -= dr / dx
        else:
            dx = self.mesh.get_nodes()[-1] - self.mesh.get_nodes()[-2]
            dr = self.equation.flow_term(self.mesh.get_nodes()[-2] + dx / 2)
            self.matrix[-1, -1] += dr / dx
            self.matrix[-1, -2] -= dr / dx
            
    def assemble_boundary(self, boundary_flags: List[bool], boundary_values: List[float]):
        # Left corner
        if boundary_flags[0]:
            self.assemble_dirichlet(0, boundary_values[0])
        else:
            self.assemble_neumann(0)
            
        if boundary_flags[-1]:
            self.assemble_dirichlet(self.mesh.get_elements[-1], boundary_values[-1])
        else:
            self.assemble_neumann(self.mesh.get_elements[-1])
            
    
    @property
    def get_K(self):
        return self.K
    
    @property
    def get_M(self):
        return self.M
    
    @property 
    def get_rhs(self):
        return self.F
            
        