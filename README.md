# GCodeSim

GCodeSim is a python program to simulate laser cutting process. Given the g-code string as input, the program simulates the laser cutting process and outputs the final work piece as a string.

Currently, the program does not support any command line parameters. To change the input, modify main.py as follows:
```
if __name__ == '__main__':
    p = TestSimulator.get_test_case_1()
    print(simulate(p[0], p[1], p[2]))
```
or equivalently you can also modify the program as follows:

```
if __name__ == '__main__':
    program = """
    G01 X2.0 Y1.00
    M01
    G01 X6.00 Y1.00
    M01
    G01 X2.00 Y3.00
    M01
    G01 X6.00 Y3.00
    M01
    G01 X0.00 Y0.00
    """
    print(simulate(program, 5, 9))
```
The above should produce the following output:
```
.........
..XXXXX..
.........
..XXXXX..
.........
```

### Build and Installation
```sh
$ git clone https://github.com/vaidyt/GCodeSim.git
$ cd GCodeSim
$ python main.py
```

NOTE

numpy is a prerequisite for the project and it can be easily installed by following the instructions here - https://numpy.org/install/


#### Description of Projects
- main.py - Contains the entry point for the program
- Simulator.py - Simulator class that does the main simulation [all main logic is in this file]
- Parser.py - Parser class that parses the g-code string and extracts relevant command and parameters
- LineSeg2D.py - Models a directed line segment in 2D
- test_simulator.py - Contains unit tests for the main "Simulate" method of the Simulator class; Also contains 5 sample inputs for the program.

License
----

MIT
