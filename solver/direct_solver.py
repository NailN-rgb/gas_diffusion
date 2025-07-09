import numpy as np
from scipy.linalg import solve

from base_solver import BaseSolver
from solver.precond.base_precond import BasePrecondtioner

class DirectSolver(BaseSolver):
    def __init__(self, tol: float = 0.000001, maxiter: int = 10000, precond: BasePrecondtioner = None):
        super().__init__(tol, maxiter, precond)
    
    def solve(self, A: np.ndarray, b: np.ndarray) -> np.ndarray:
        return solve(A, b)