# GCodeSim

GCodeSim is a python program to simulate laser cutting process. Given the g-code string as input, the program simulates the laser cutting process and outputs the final cut pattern as a string.

### Usage
```sh
$ python main.py <infile> <n_rows> <n_cols>
```
- infile: Input g-code file
- n_rows: Number of rows in the grid
- n_cols: Number of rows in the grid

#### Mode 1 (no parameters):

Mode 1 simply simulates one of the test cases

```sh
$ BRep.CLI
```

#### Mode 2 (with three parameters):

Mode 2 can be used to run the program for any user defined g-code file for any required grid dimensions of size n_rows X n_cols. In this mode, the output is written to a file (instead of writing it to the screen)

### Build and Installation
```sh
$ git clone https://github.com/vaidyt/GCodeSim.git
$ cd GCodeSim
$ python main.py
```

#### NOTE

- The program was tested in python 3.9.1
- NumPy is a prerequisite for the project and it can be easily installed by following the instructions here - https://numpy.org/install/ 


#### Description of Projects
- main.py - Contains the entry point for the program
- Simulator.py - Simulator class that does the main simulation [all main logic is in this file]
- Parser.py - Parser class that parses the g-code string and extracts relevant commands and parameters
- LineSeg2D.py - Models a directed line segment in 2D; This class has the method to compute the distance of a pt to the line segment
- test_simulator.py - Contains unit tests for the main "simulate" method of the Simulator class; Also contains 5 sample inputs for the program.
- test_LineSeg2D.py - Contains unit tests for "distance_from_pt" of LineSeg2D class
- FormLogic_Logo - Contains the G-Code for the FormLogic logo. It also contains a MATLAB script and additional file/pictures used to generate this g-code. The output of the simulator for this g-code can be found [here](https://github.com/vaidyt/GCodeSim/blob/main/Formlogic_Logo/FormLogic_logo_generated_output.txt)

### ToDos
- __make_laser_cut method of Simulator class needs to be vectorized
- Additional error checks in Parser class (to handle invalid coordinates) to be implemented


License
----

MIT
