from base_equation import Equation
from LinearPVT import LinearPVT

class LinearEquation1D(Equation):
    def flow_term(self, x: float) -> float:
        return 1
    
    # phi * ct
    def accumulative_term(self, x: float) -> float:
        return 1
    
    def source_term(self, x: float) -> float:
        return 1
    
    def boundary_condition(self, x: float = 0, y: float = 0) -> float:
        return 0
    
    def is_linear(self):
        return True
        