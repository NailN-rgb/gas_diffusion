import numpy as np
from scipy.sparse.linalg import gmres

from base_solver import BaseSolver

class GMRESSolver(BaseSolver):
    def solve(self, A: np.ndarray, b: np.ndarray) -> np.ndarray:
        self.preconditioner.build(A)
        M = self.preconditioner.get_linear_operator()
        x, info = gmres(A, b, tol=self.tol, restart=50, maxiter=self.maxiter, M=M)
        if info:
            raise RuntimeError(f"GMRES did not converge, info = {info}")
        return x