import numpy as np
import scipy.sparse

from equation.base_equation import Equation
from mesh1D.mesh1D import Mesh1D


def assemble_system(
    mesh: Mesh1D, 
    equation: Equation, 
    dt, 
    pold
):
    
    # get mesh
    mesh_nodes = mesh.get_nodes
    
    N = len(mesh_nodes)
    
    # evaluate lambda values 
    lam = equation.flow_term()
    
    # evaluate acc term 
    acc = equation.accumulative_term()
    
    # Fill tridiagonal stiffness matrix
    a, b, c, rhs = (np.zeros(N) for _ in range(4))
    
    for i in range(1, N - 1):
        a[i]   = lam / (mesh_nodes[i] - mesh_nodes[i - 1])
        c[i]   = lam / (mesh_nodes[i + 1] - mesh_nodes[i])
        b[i]   = - acc / dt * (mesh_nodes[i + 1] - mesh_nodes[i - 1]) / 2 - a[i] - c[i]
        rhs[i] = - acc / dt * (mesh_nodes[i + 1] - mesh_nodes[i - 1]) / 2 * pold[i]
    
    # Left boundary
    c[0] = lam / (mesh_nodes[1] - mesh_nodes[0])
    b[0] = -c[0] - acc / dt * (mesh_nodes[1] - mesh_nodes[0]) 
    rhs[0] = -acc / dt * (mesh_nodes[1] - mesh_nodes[0]) * pold[0]
    
    # Right boundary
    a[N - 1] = lam / (mesh_nodes[N - 1] - mesh_nodes[N - 2])
    b[N - 1] = -a[N - 1] - acc / dt * (mesh_nodes[N - 1] - mesh_nodes[N - 2]) 
    rhs[N - 1] = -acc / dt * (mesh_nodes[N - 1] - mesh_nodes[N - 2]) * pold[N - 1]
    
    
    A = scipy.sparse.diags(
        diagonals = [a[1:], b, c[:-1]],
        offsets=[-1, 0, 1],
        shape=(N, N),
        format='csr'
    )
    
    return A, rhs
    