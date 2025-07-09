import numpy as np
from abc import ABC, abstractmethod

from solver.precond.base_precond import BasePrecondtioner
from solver.precond.identity_precond import IdentityPreconditioner


class BaseSolver(ABC):
    def __init__(self, tol: float = 1e-6, maxiter: int = 10000, precond: BasePrecondtioner = None):
        self.tol = tol
        self.maxiter = maxiter
        self.preconditioner = precond or IdentityPreconditioner()
    
    @abstractmethod
    def solve(self, A: np.ndarray, b: np.ndarray) -> np.ndarray:
        pass