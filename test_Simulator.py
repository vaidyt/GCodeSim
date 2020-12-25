from unittest import TestCase
from Simulator import Simulator


class TestSimulator(TestCase):

    @staticmethod
    def get_test_case_1() -> list:
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

    @staticmethod
    def get_test_case_2() -> list:
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

    @staticmethod
    def get_test_case_3() -> list:
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

    @staticmethod
    def get_test_case_4() -> list:
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

    @staticmethod
    def get_test_case_5() -> list:
        program = """
        M01
        G01 X4.0 Y3.0
        M01
        G01 X0.0 Y0.0
        """
        return program, 4, 5

    def test_1(self):
        p = TestSimulator.get_test_case_1()
        sim = Simulator(p[0], p[1], p[2])
        computed = sim.simulate()
        reference = """.........\n..XXXXX..\n.........\n..XXXXX..\n.........\n"""
        self.assertTrue(reference == computed)

    def test_2(self):
        p = TestSimulator.get_test_case_2()
        sim = Simulator(p[0], p[1], p[2])
        computed = sim.simulate()
        reference = """......XXX\n........X\nX...X...X\nX........\nXXX......\n"""
        self.assertTrue(reference == computed)

    def test_3(self):
        p = TestSimulator.get_test_case_3()
        sim = Simulator(p[0], p[1], p[2])
        computed = sim.simulate()
        reference = """....X....\n..XXXXX..\n.........\n..XXXXX..\n....X....\n"""
        self.assertTrue(reference == computed)

    def test_4(self):
        p = TestSimulator.get_test_case_4()
        sim = Simulator(p[0], p[1], p[2])
        computed = sim.simulate()
        reference = """..XXX..\nXX...XX\n..XXX..\n"""
        self.assertTrue(reference == computed)

    def test_5(self):
        p = TestSimulator.get_test_case_5()
        sim = Simulator(p[0], p[1], p[2])
        computed = sim.simulate()
        reference = """X....\n.XX..\n..XX.\n....X\n"""
        self.assertTrue(reference == computed)