# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Simulator


def simulate(program: str, n_rows: int, n_cols: int) -> str:
    sim_obj = Simulator.Simulator(program, n_rows, n_cols)
    return sim_obj.simulate()


def get_test_case_1():
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
    return program, 5, 9


def get_test_case_2():
    program = """
       G01 X0.0 Y2.00
       M01
       G01 X0.00 Y4.00
       G01 X2.00 Y4.00
       M01
       G01 X4.00 Y2.00
       M01
       M01
       G01 X6.00 Y0.00
       M01
       G01 X8.00 Y0.00
       G01 X8.00 Y2.00
       M01
       G01 X0.00 Y0.00
       """
    return program, 5, 9


def get_test_case_3():
    program = """
        G01 X2.00 Y1.00
        M01
        G01 X6.00 Y1.00
        M01
        G01 X2.00 Y3.00
        M01
        G01 X4.00 Y3.00
        G01 X4.00 Y4.00
        G01 X5.00 Y3.00
        G01 X6.00 Y3.00
        M01
        G01 X4.00 Y0.00
        M01
        M01
        G01 X0.00 Y0.00
        """
    return program, 5, 9


def get_test_case_4():
    program = """
        G01 X0.00 Y1.00
        M01
        G01 X1.10 Y1.00
        G01 X2.00 Y2.00
        G01 X4.00 Y2.00
        G01 X5.00 Y1.00
        G01 X6.00 Y1.00
        M01
        G01 X2.00 Y0.00
        M01
        G01 X4.00 Y0.00
        M01
        G01 X0.00 Y0.00
        """
    return program, 3, 7


def get_test_case_5():
    program = """
       M01
       G01 X4.0 Y3.0
       M01
       G01 X0.0 Y0.0
       """
    return program, 4, 5


if __name__ == '__main__':
    p = get_test_case_2()
    print(simulate(p[0], p[1], p[2]))


