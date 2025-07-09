from abc import ABC, abstractmethod
import numpy as np

from mesh1D.mesh1D import Mesh1D
from equation.base_equation import Equation
from assembler.base_assembler import BaseAssembler
from timeIntergator.base_integrator import BaseIntegrator

class BaseIntegrator(BaseIntegrator):
    def __init__(self, mesh: Mesh1D, equation: Equation, assembler: BaseAssembler, dt: float, T: float):
        super().__init__()
        
    def solve_layer(self, u0: np.ndarray, t: float) -> np.ndaraay:
        u = u0.copy()
        self.u_history.append(u.copy())
        
        self.assembler.assemble_global()
        M, K, F = self.assembler.get_M(), self.assembler.get_K(), self.assembler.get_rhs() 
        
        A = M + self.dt * K
        b = M @ u + self.dt * F
        
        # TODO: apply BC
        
        # TODO: get solver types
        
        return u