import numpy as np
import matplotlib.pyplot as plt

from mesh1D.mesh1D import Mesh1D


def print_solution(
    mesh_data: Mesh1D,
    last_solution: np.ndarray
):
    plt.figure("Solution at last time layer")
    plt.plot(mesh_data.nodes, last_solution[0:-1], "ro")
    
    plt.xlabel("x")
    plt.ylabel("p")
    
    plt.axis((mesh_data.x_start, mesh_data.x_end, -100, 400))
    
    plt.savefig("visualization/last_sol.png")
    
    

def solution_animation():
    pass