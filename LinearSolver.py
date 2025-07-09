import scipy

from fe1D.linear_element import LinearElement
from mesh1D.mesh1D import Mesh1D
from pvts.LinearPVT import LinearPVT
from equation.linear_equation1D import LinearEquation1D
from CVFEAssembler.cvfe_assembler import assemble_system
from solver.bcgstab_solver import BCGStabSolver


def LinearSolver():
    linear_element = LinearElement()
    
    # Initialize mesh object
    OneDimMesh = Mesh1D(
        0.0,
        1.0,
        100,
        0.5,
        linear_element
    )
    
    # Initialize PVT object
    PVT_Model = LinearPVT()
    
    Equation_Data = LinearEquation1D(PVT_Model)
    
    # Initial pressure at nodes
    Initial_Pressure = Equation_Data.initial_condition(OneDimMesh.get_nodes_count, 340.23)
    
    p_old = Initial_Pressure
    
    # Initialize equation system solver
    Solver = BCGStabSolver(tol=0.001)
    
    # Time loop
    for i in range(1, 100):
        # Assemble system
        Stifness_Matrix, Force_Vector = assemble_system(
            OneDimMesh,
            Equation_Data,
            0.001,
            p_old
        )
        
        p_old = scipy.sparse.linalg.spsolve(Stifness_Matrix, Force_Vector)
        
        print("Solved for " + str(i) + " time layer")
        
    print(p_old[-1])
        
        
    
    print("Linear Solver Finished")