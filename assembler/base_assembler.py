from abc import ABC, abstractmethod
from typing import List, Tuple
import numpy as np

from equation.base_equation import Equation
from fe1D.base_element import Base_element
from mesh1D.mesh1D import Mesh1D

class BaseAssembler():
    @abstractmethod
    def __init__(self, element: Base_element) -> None:
        pass
    
    @abstractmethod
    def assemble_element(self, elem_nodes: List[float], equation: Equation) -> Tuple[List[List[float]], List[List[float]], List[float]]:
        pass
    
    def assemble_global(self, mesh: Mesh1D, equation: Equation) -> Tuple[List[List[float]], List[List[float]], List[float]]:
        n_nodes = mesh.get_nodes_count()
        
        M = np.zeros((n_nodes, n_nodes))
        K = np.zeros((n_nodes, n_nodes))
        F = np.zeros(n_nodes)
        
        mesh_nodes    = mesh.get_nodes()
        mesh_elements = mesh.get_elements()
        
        for elem_nodes in mesh_elements:
            x_coords = [mesh_nodes[i] for i in range elem_nodes]
            local_M, local_K, local_F = self.assemble_element(x_coords, equation)
            
            for i_local, i_global in enumerate(elem_nodes):
                F[i_global] += local_F[i_local]
                for j_local, j_global in enumerate(elem_nodes):
                    M[i_global, j_global] += local_M[i_local, j_local]
                    K[i_global, j_global] += local_K[i_local, j_local]
                    
        return M, K, F
            