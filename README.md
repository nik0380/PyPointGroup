# PointGroup Software

The **PointGroup** software allows you to visualize point symmetry groups (*OpenGL*).

## Main features of the program
1. Visualization of a point symmetry group selected from the list.
2. Visualization of the point symmetry group given by the group generators.
3. Group generators can be specified in the form of matrices, as well as selected from the list.
4. Construction of the Cayley table for the symmetry group.

## Installation
To install the software use the command:

`pip install PyPointGroup`

### Dependencies

The package uses the following dependencies:
1. `NumPy`
2. `PyQt5` or `PyQt >= 5.0`
3. `PyOpenGL`
4. `PyShortCuts` (optionally, to create a program shortcut)

### Conda/Anaconda

To install the software use the command:

`conda install -c nik0380 pypointgroup`

Conda environment: 

    name: pointgroup
    channels:
    - conda-forge
    dependencies:
    - numpy
    - PyQt>=5.0
    - PyOpenGL
    - pip
    - pip:
          - PyPointGroup


## Running the program

To run the program use the command

`pypointgroup`

After starting the program, you can create a shortcut to the **PointGroup**.
To do this, in the **Tool** menu item, select *"Create shortcuts..."*. 
You must first install the `PyShortCuts` package:

`pip install pyshortcuts`