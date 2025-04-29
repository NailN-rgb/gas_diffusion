from base_element import Base_element
from typing import List, Tuple


class LinearElement(Base_element):
    def num_nodes(self) -> int:
        return 2
    
    def shape_function(self, i: int, x: float) -> float:
        if i == 0:
            return 1 / 2 * (1 - x)
        elif i == 1:
            return 1 / 2 * (1 + x)
        else:
            raise IndexError("Unable to get shape function with invalid index")
    
    def shape_function_der(self, i: int, x: float) -> float:
        if i == 0:
            return - 1 / 2
        elif i == 1:
            return 1 / 2
        else:
            raise IndexError("Unable to get shape function derivative with invalid index")
        
    
    def integration_points(self) -> List[Tuple[float, float]]:
        return [(0.0, 2.0)]