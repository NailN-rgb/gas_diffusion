from typing import List, Tuple

from base_assembler import BaseAssembler
from ..fe1D.base_element import Base_element
from ..equation.base_equation import Equation

class Assembler1D(BaseAssembler):
    def __init__(self, element: Base_element):
        self.element = element
        
    def assemble_element(self, elem_nodes: List[float], equation: Equation) -> Tuple[List[List[float]], List[List[float]], List[float]]:
        n = self.element.num_nodes()
        
        # Init local matrixes with zero matrix
        M = [[0.0 for _ in range(n)] for _ in range(n)]
        K = [[0.0 for _ in range(n)] for _ in range(n)]
        F = [0.0 for _ in range(n)]
        
        for xi, w in self.element.integration_points():
            # transform node point from basis elem with shape fuctions
            x  = sum(self.element.shape_function(i, xi)     * elem_nodes[i] for i in range(n))
            dx = sum(self.element.shape_function_der(i, xi) * elem_nodes[i] for i in range(n))
            
            jacobian = abs(dx)
            
            acc = equation.accumulative_term(x)
            D   = equation.flow_term(x)
            f   = equation.source_term(x)
            
            for i in range(n):
                # get i-shape functions
                Ni  = self.element.shape_function(i, xi)
                dNi = self.element.shape_function_der(i, xi) / dx
                
                F[i] = Ni * f * w * jacobian
                
                for j in range(n):
                    # get j- shape functions
                    Nj  = self.element.shape_function(j, xi)
                    dNj = self.element.shape_function_der(j, xi) / dx
                    
                    M[i][j] += acc * Ni * Nj * w * jacobian
                    K[i][j] +=   D * Ni * Nj * w * jacobian
                    
        return M, K, F