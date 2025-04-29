mesh1D    - return mesh at 1D domain
pvts      - return PVT params + formation params 
fe1D      - realize types of Finite Elements
equation  - return disctritized parts of parabolic equation
assembler - get local matrix + rhs for element type discretized by FVM 

solver    - solve global matrix + rhs with different methods
precond   - preconditioners for solving procedures
timeInt   - integrate by time steps using different schemes
postproc  - solution postprocess (get PVF)