Cladding Pin Cells
--------------------

This is a basic repo with files to perform quick analysis about the impact of
different cladding materials on reactor neutronics with the use of simple
pin-cell calculations.

* mat_defn.py: PyNE based script to convert simple engineering descriptions of
  materials to MCNP input definitions.

* triangle.inp: input file with triangular pitch, nominally with a half-pitch
  of 0.86603 cm.  The cladding thickness can be modified to seek any fixed
  eigenvalue, or the material can be changed to see the change in eigenvalue,
  or some combination of those.
