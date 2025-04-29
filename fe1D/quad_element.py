from base_element import Base_element
from typing import List, Tuple


class QuadraticElement(Base_element):
    def num_nodes(self) -> int:
        pass
    
    def shape_function(self, i: int, x: float) -> float:
        pass
    
    def shape_function_der(self, i: int, x: float) -> float:
        pass    
    
    def integration_points(self) -> List[Tuple[float, float]]:
        pass