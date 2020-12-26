# Entry point for the simulator
import time
import Simulator
from test_Simulator import TestSimulator
import sys
import os


def simulate(program: str, n_rows: int, n_cols: int) -> str:
    if n_rows <= 0 or n_cols <= 0:
        print("Error: Invalid grid dimensions; n_rows and n_cols should be strictly greater than 0")
        return ""

    sim_obj = Simulator.Simulator(program, n_rows, n_cols)
    return sim_obj.simulate(True)


def print_usage():
    print("Error: Invalid number of parameters")
    print("Usage: \nOption1 -> python main.py")
    print("or")
    print("Option2 -> python main.py <gcode_file_name> <n_rows> <n_cols>")


if __name__ == '__main__':
    if len(sys.argv) == 1:
        # Option 1: python main.py
        p = TestSimulator.get_test_case_2()
        write_to_file = False
        out_file_name = "temp.txt"
    elif len(sys.argv) == 4:
        # Option 2: python main.py <gcode_file_name> <n_rows> <n_cols>
        p = [None] * 3
        p[0] = TestSimulator.read_file(sys.argv[1])
        if not p[0]:
            sys.exit()

        p[1] = int(sys.argv[2])
        p[2] = int(sys.argv[3])
        out_file_name = os.path.splitext(sys.argv[1])[0] + ".txt"
        write_to_file = True
    else:
        print_usage()
        sys.exit()

    print('Simulation started...')
    t = time.time()

    # Call the main simulate method
    s = simulate(p[0], p[1], p[2])

    elapsed = time.time() - t
    print('Simulation completed in ' + "{:.3f}".format(elapsed) + " s")

    if write_to_file:
        TestSimulator.write_to_file(s, out_file_name)
        print("Output written to " + out_file_name)
    else:
        print(s)

