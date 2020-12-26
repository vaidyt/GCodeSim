from unittest import TestCase
from LineSeg2D import LineSeg2D
import numpy as np
import math


# Unit tests for distance to a point from a line segment
class TestLineSeg2D(TestCase):
    def test_1(self):
        print("\nRunning LineSeg2D Test 1...")
        # Horizontal line segment
        l = LineSeg2D(0, 0, 1, 0)
        # test Pt
        pt = [0.5, 0.5]
        d = l.distance_from_pt(pt)
        self.assertEqual(0.5, d)

    def test_2(self):
        print("Running LineSeg2D Test 2...")
        # Vertical line segment
        l = LineSeg2D(0, 0, 0, 1)
        # test Pt
        pt = [0.5, 0.5]
        d = l.distance_from_pt(pt)
        self.assertEqual(0.5, d)

    def test_3(self):
        print("Running LineSeg2D Test 3...")
        # 45 degree line segment
        l = LineSeg2D(0, 0, 1, 1)
        # test Pt
        pt = [0.5, 0.5]
        d = l.distance_from_pt(pt)
        self.assertTrue(d <= np.finfo(float).eps)

    def test_4(self):
        print("Running LineSeg2D Test 4...")
        # Arbitrary inclined line segment
        l = LineSeg2D(-20, 0, 0, 10)
        # test Pt
        pt = [-5, -5]
        d = l.distance_from_pt(pt)
        self.assertAlmostEqual(11.180339887498949, d)

    def test_5(self):
        print("Running LineSeg2D Test 5...")
        # Arbitrary inclined line segment
        l = LineSeg2D(-20, 0, 0, 10)
        # test Pt is one of the end points
        pt = [0, 10]
        d = l.distance_from_pt(pt)
        self.assertEqual(0, d)

    def test_6(self):
        print("Running LineSeg2D Test 6...")
        # Arbitrary inclined line segment
        l = LineSeg2D(-20, 0, 0, 10)
        # test Pt is one of the end points
        pt = [-20, 0]
        d = l.distance_from_pt(pt)
        self.assertEqual(0, d)

    def test_7(self):
        print("Running LineSeg2D Test 7...")
        # 45 degree line segment
        l = LineSeg2D(0, 0, 1, 1)
        # test Pt
        pt = [0, 1]
        d = l.distance_from_pt(pt)
        self.assertAlmostEqual(1/math.sqrt(2), d)

    def test_8(self):
        print("Running LineSeg2D Test 8...")
        # 45 degree line segment
        l = LineSeg2D(0, 0, 1, 1)
        # test Pt
        pt = [1, 0]
        d = l.distance_from_pt(pt)
        self.assertAlmostEqual(1/math.sqrt(2), d)

    def test_9(self):
        print("Running LineSeg2D Test 9...")
        # 45 degree line segment
        l = LineSeg2D(0, 0, 1, 1)
        # test Pt
        pt = [-1, -1]
        d = l.distance_from_pt(pt)
        self.assertAlmostEqual(math.sqrt(2), d)

    def test_10(self):
        print("Running LineSeg2D Test 10...")
        # 45 degree line segment
        l = LineSeg2D(0, 0, 1, 1)
        # test Pt
        pt = [-1, 1]
        d = l.distance_from_pt(pt)
        self.assertAlmostEqual(math.sqrt(2), d)

    def test_11(self):
        print("Running LineSeg2D Test 11...")
        # 45 degree line segment
        l = LineSeg2D(0, 0, 1, 1)
        # test Pt
        pt = [-1, 0]
        d = l.distance_from_pt(pt)
        self.assertEqual(1, d)

    def test_12(self):
        print("Running LineSeg2D Test 12...")
        # 45 degree line segment
        l = LineSeg2D(0, 0, 1, 1)
        # test  is far away on positive x-axis
        pt = [100, 0]
        d = l.distance_from_pt(pt)
        self.assertAlmostEqual(99.005050376230813, d)

    def test_13(self):
        print("Running LineSeg2D Test 13...")
        # 45 degree line segment
        l = LineSeg2D(0, 0, 1, 1)
        # test  is far away on negative x-axis
        pt = [-100, 0]
        d = l.distance_from_pt(pt)
        self.assertEqual(100, d)

    def test_14(self):
        print("Running LineSeg2D Test 14...")
        # 45 degree line segment
        l = LineSeg2D(0, 0, 1, 1)
        # test  is far away on negative x-axis
        pt = [-100, 0]
        d = l.distance_from_pt(pt)
        self.assertEqual(100, d)

    def test_15(self):
        print("Running LineSeg2D Test 15...")
        # 45 degree line segment
        l = LineSeg2D(0, 0, 1, 1)
        # test  is far away on negative y-axis
        pt = [0, -100]
        d = l.distance_from_pt(pt)
        self.assertEqual(100, d)

    def test_16(self):
        print("Running LineSeg2D Test 15...")
        # degenerate case
        l = LineSeg2D(0, 0, 0, 0)
        # test  is far away on negative y-axis
        pt = [1, 1]
        d = l.distance_from_pt(pt)
        self.assertEqual(math.sqrt(2), d)

    def test_17(self):
        print("Running LineSeg2D Test 15...")
        # degenerate case
        l = LineSeg2D(0, 0, np.finfo(float).eps, np.finfo(float).eps)
        # test  is far away on negative y-axis
        pt = [1, 1]
        d = l.distance_from_pt(pt)
        self.assertAlmostEqual(math.sqrt(2), d)