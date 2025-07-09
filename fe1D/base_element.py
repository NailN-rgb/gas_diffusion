from abc import ABC, abstractmethod
from typing import List, Tuple

class Base_element(ABC):
    def __init__(self, ):
        pass
    
    @abstractmethod
    def num_nodes(self) -> int:
        pass
    
    @abstractmethod
    def shape_function(self) -> float:
        pass
    
    @abstractmethod
    def shape_function_der(self) -> float:
        pass
    
    @abstractmethod
    def integration_points(self) -> List[Tuple[float, float]]:
        pass
     