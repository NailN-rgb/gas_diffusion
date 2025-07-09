from scipy.sparse.linalg import LinearOperator
import numpy as np
from scipy.sparse import csc_matrix

from solver.precond.base_precond import BasePrecondtioner

class IdentityPreconditioner(BasePrecondtioner):
    def build(self, A: np.ndarray) -> None:
        self.n = A.shape[0]
    
    def get_linear_operator(self) -> LinearOperator:
        return LinearOperator((self.n, self.n), matvec=lambda x: x)