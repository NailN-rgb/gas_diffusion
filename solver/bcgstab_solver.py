import numpy as np
from scipy.sparse.linalg import bicgstab

from base_solver import BaseSolver

class BCGStabSolver(BaseSolver):
    def solve(self, A: np.ndarray, b: np.ndarray) -> np.ndarray:
        self.preconditioner.build(A)
        M = self.preconditioner.get_linear_operator()
        x, info = bicgstab(A, b, tol=self.tol, maxiter=self.maxiter, M=M)
        if info:
            raise RuntimeError(f"GMRES did not converge, info = {info}")
        return x