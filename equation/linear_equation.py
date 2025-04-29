from base_equation import Equation
from LinearPVT import LinearPVT

class LinearEquation(Equation):
    def flow_term(self, x: float, y: float) -> float:
        return super().flow_term(x, y)
    
    def accumulative_term(self, x: float, y: float) -> float:
        return super().accumulative_term(x, y)
    
    def source_term(self, x: float, y: float) -> float:
        return super().source_term(x, y)
    
    def boundary_condition(self, x: float = 0, y: float = 0, t: float = 0) -> float:
        return super().boundary_condition(x, y, t)
    
    def is_linear(self):
        return super().is_linear()
        