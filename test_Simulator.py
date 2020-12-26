from unittest import TestCase
from Simulator import Simulator
import os


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

    @staticmethod
    def get_test_case_6() -> list:

        program = TestSimulator.read_file(".\\Formlogic_Logo\\FormLogic.gcode")
        return program, 200, 200

    @staticmethod
    def read_file(file_name) -> str:
        if not os.path.isfile(file_name):
            print("Error: " + file_name + " doesn't exist! Please make sure the input file exists!")
            return ""
        file = open(file_name)
        program = file.read()
        file.close()
        return program

    @staticmethod
    def write_to_file(str_out: str, file_name: str):
        text_file = open(file_name, "w")
        text_file.write(str_out)
        text_file.close()

    def test_1(self):
        print("\nRunning Simulator Test 1...")
        p = TestSimulator.get_test_case_1()
        sim = Simulator(p[0], p[1], p[2])
        computed = sim.simulate(True)
        reference = """.........\n..XXXXX..\n.........\n..XXXXX..\n.........\n"""
        self.assertTrue(reference == computed)

    def test_2(self):
        print("Running Simulator Test 2...")
        p = TestSimulator.get_test_case_2()
        sim = Simulator(p[0], p[1], p[2])
        computed = sim.simulate(True)
        reference = """......XXX\n........X\nX...X...X\nX........\nXXX......\n"""
        self.assertTrue(reference == computed)

    def test_3(self):
        print("Running Simulator Test 3...")
        p = TestSimulator.get_test_case_3()
        sim = Simulator(p[0], p[1], p[2])
        computed = sim.simulate(True)
        reference = """....X....\n..XXXXX..\n.........\n..XXXXX..\n....X....\n"""
        self.assertTrue(reference == computed)

    def test_4(self):
        print("Running Simulator Test 4...")
        p = TestSimulator.get_test_case_4()
        sim = Simulator(p[0], p[1], p[2])
        computed = sim.simulate(True)
        reference = """..XXX..\nXX...XX\n..XXX..\n"""
        self.assertTrue(reference == computed)

    def test_5(self):
        print("Running Simulator Test 5...")
        p = TestSimulator.get_test_case_5()
        sim = Simulator(p[0], p[1], p[2])
        computed = sim.simulate(True)
        reference = """X....\n.XX..\n..XX.\n....X\n"""
        self.assertTrue(reference == computed)

    def test_6(self):
        print("Running Simulator Test 6...")
        p = TestSimulator.get_test_case_6()
        sim = Simulator(p[0], p[1], p[2])
        computed = sim.simulate(True)
        reference = TestSimulator.read_file(".\\Formlogic_Logo\\Formlogic_logo_reference.txt")
        self.assertTrue(reference == computed)