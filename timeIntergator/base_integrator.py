from abc import ABC, abstractmethod
import numpy as np

from mesh1D.mesh1D import Mesh1D
from equation.base_equation import Equation
from assembler.base_assembler import BaseAssembler

class BaseIntegrator(ABC):
    def __init__(self, mesh: Mesh1D, equation: Equation, assembler: BaseAssembler, dt: float, T: float):
        self.mesh = mesh
        self.equation = equation
        self.dt = dt
        self.assembler = assembler
        self.u_history = []
        
    @abstractmethod
    def solve_layer(self, u0: np.ndarray, t: float) -> np.ndaraay:
        pass