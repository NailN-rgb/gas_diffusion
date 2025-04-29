from scipy.sparse.linalg import LinearOperator
from scipy.sparse.linalg import spilu
from scipy.sparse import csc_matrix
import numpy as np

from base_precond import BasePrecondtioner

class IdentityPreconditioner(BasePrecondtioner):
    def build(self, A: np.ndarray) -> None:
        A_csc = csc_matrix(A)
        self.ilu = spilu(A_csc)
    
    def get_linear_operator(self) -> LinearOperator:
        return LinearOperator(self.ilu.shape, matvec=self.ilu.solve)