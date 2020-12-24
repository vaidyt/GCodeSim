# Entry point for the simulator
import Simulator
from test_Simulator import TestSimulator


def simulate(program: str, n_rows: int, n_cols: int) -> str:
    sim_obj = Simulator.Simulator(program, n_rows, n_cols)
    return sim_obj.simulate()


if __name__ == '__main__':
    p = TestSimulator.get_test_case_1()
    print(simulate(p[0], p[1], p[2]))
