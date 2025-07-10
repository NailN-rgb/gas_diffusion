import scipy

from fe1D.linear_element import LinearElement
from mesh1D.mesh1D import Mesh1D
from pvts.LinearPVT import LinearPVT
from equation.linear_equation1D import LinearEquation1D
from CVFEAssembler.cvfe_assembler import assemble_system
from solver.bcgstab_solver import BCGStabSolver
from visualization.visualizators import print_solution


def LinearSolver():
    linear_element = LinearElement()
    
    # Initialize mesh object
    OneDimMesh = Mesh1D(
        x_start=0.0,
        x_end=1.0,
        min_h=0.05,
        max_h=0.5,
        well_x=0.5,
        element_type=linear_element,
        N=100,
        mesh_type="geometric"
    )
    
    # Initialize PVT object
    PVT_Model = LinearPVT()
    
    Equation_Data = LinearEquation1D(PVT_Model)
    
    # Initial pressure at nodes
    Initial_Pressure = Equation_Data.initial_condition(OneDimMesh.get_nodes_count, 340.)
    
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
    
    print_solution(OneDimMesh, p_old)
        
        
    
    print("Linear Solver Finished")