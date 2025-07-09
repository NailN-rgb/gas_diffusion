import numpy as np

from equation.base_equation import Equation
from pvts.LinearPVT import LinearPVT

class LinearEquation1D(Equation):
    # TODO: Overload for abstract pvt model
    def __init__(self, pvt: LinearPVT):
        self.pvt = pvt
    
    # lambda
    def flow_term(self, x: float = 0.0) -> float:
        return self.pvt.get_k / (self.pvt.get_mu * self.pvt.get_B)
    
    # phi * ct
    def accumulative_term(self, x: float = 0.0) -> float:
        return self.pvt.get_phi * self.pvt.get_ct
    
    def source_term(self, x: float = 0.0) -> float:
        return 1
    
    def initial_condition(self, nodes_count: np.ndarray, init_pressure: float):
        return np.ones(nodes_count) * init_pressure
    
    # unused
    def boundary_condition(self, x: float = 0, y: float = 0) -> float:
        return 0
    
    def is_linear(self):
        return True
        