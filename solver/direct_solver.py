import numpy as np
from scipy.linalg.solve import direct_solver

from base_solver import BaseSolver

class DirectSolver(BaseSolver):
    def solve(self, A: np.ndarray, b: np.ndarray) -> np.ndarray:
        return direct_solver(A, b)