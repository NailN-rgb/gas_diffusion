from abc import ABS, abstractmethod

class Equation(ABC):
    @abstractmethod
    def flow_term(self, x: float, y: float) -> float:
        pass
    
    @abstractmethod
    def accumulative_term(self, x: float, y: float) -> float:
        pass
    
    @abstractmethod
    def source_term(self, x: float, y: float) ->float:
        pass
    
    @abstractmethod
    def boundary_condition(self, x: float = 0.0, y: float = 0.0, t: float = 0.0) -> float:
        pass
    
    @abstractmethod
    def is_linear(self):
        return True