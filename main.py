# Entry point for the simulator
import Simulator
from test_Simulator import TestSimulator


def simulate(program: str, n_rows: int, n_cols: int) -> str:
    if n_rows <=0 or n_cols <=0:
        print("Error: Invalid grid dimensions; n_rows and n_cols should be strictly greater than 0")
        return ""

    sim_obj = Simulator.Simulator(program, n_rows, n_cols)
    return sim_obj.simulate()


if __name__ == '__main__':
    p = TestSimulator.get_test_case_5()
    print(simulate(p[0], p[1], p[2]))