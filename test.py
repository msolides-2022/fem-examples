import dolfinx # FEM in python
import matplotlib.pyplot as plt
import ufl # variational formulations
import numpy as np
from mpi4py import MPI
from petsc4py.PETSc import ScalarType
import gmsh # Mesh generation
import pyvista # visualisation in python notebook

# Geometry
R_i = 1.0 # Radius of the inclusion
R_e = 6.9  # Radius of the matrix (whole domain)
aspect_ratio = 1.0 # start with a circle, otherwise ellipse

# Material
E_m = 0.8 # Young's modulus in matrix
nu_m = 0.35 # Poisson's ratio in matrix
E_i = 11.0 # Young's modulus of inclusion
nu_i = 0.3 # Poisson's ratio in inclusion

R_i = 1.
mesh_size = R_i/5
mesh_order = 1
mesh_comm = MPI.COMM_WORLD
model_rank = 0
gmsh.initialize()
facet_names = {"inner_boundary": 1, "outer_boundary": 2}
cell_names = {"inclusion": 1, "matrix": 2}
model = gmsh.model()
model.add("Disk")
model.setCurrent("Disk")
gdim = 2 # geometric dimension of the mesh
inner_disk = gmsh.model.occ.addDisk(0, 0, 0, R_i, aspect_ratio * R_i)
outer_disk = gmsh.model.occ.addDisk(0, 0, 0, R_e, R_e)
whole_domain = gmsh.model.occ.fragment([(gdim, outer_disk)], [(gdim, inner_disk)])
gmsh.model.occ.synchronize()
# Add physical tag for bulk
inner_domain = whole_domain[0][0]
outer_domain = whole_domain[0][1]
model.addPhysicalGroup(gdim, [inner_domain[1]], tag=cell_names["inclusion"])
model.setPhysicalName(gdim, inner_domain[1], "Inclusion")
model.addPhysicalGroup(gdim, [outer_domain[1]], tag=cell_names["matrix"])
model.setPhysicalName(gdim, outer_domain[1], "Matrix")
# Add physical tag for boundaries
lines = gmsh.model.getEntities(dim=1)
inner_boundary = lines[1][1]
outer_boundary = lines[0][1]
gmsh.model.addPhysicalGroup(1, [inner_boundary], facet_names["inner_boundary"])
gmsh.model.addPhysicalGroup(1, [outer_boundary], facet_names["outer_boundary"])
gmsh.option.setNumber("Mesh.CharacteristicLengthMin",mesh_size)
gmsh.option.setNumber("Mesh.CharacteristicLengthMax",mesh_size)
model.mesh.generate(gdim)
gmsh.option.setNumber("General.Terminal", 1)
model.mesh.setOrder(mesh_order)
gmsh.option.setNumber("General.Terminal", 0)
# Import the mesh in dolfinx
from dolfinx.io import gmshio
domain, cell_tags, facet_tags = gmshio.model_to_mesh(model, mesh_comm, model_rank, gdim=gdim)
domain.name = "composite"
cell_tags.name = f"{domain.name}_cells"
facet_tags.name = f"{domain.name}_facets"
gmsh.finalize()
