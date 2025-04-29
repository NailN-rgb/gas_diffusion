from abc import ABC, abstractmethod
import numpy as np
from scipy.sparse.linalg import LinearOperator
from scipy.sparse import csc_matrix

class BasePrecondtioner(ABC):
    @abstractmethod
    def build(self, A: np.ndarray) -> None:
        pass
    
    @abstractmethod
    def get_linear_operator(self) -> LinearOperator:
        pass