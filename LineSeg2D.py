import numpy as np
from numpy import linalg as la


# LineSeg2D class that models a line segment in 2D
class LineSeg2D:

    # Constructor - creates a directed line segment between (x1,y1) and (x2,y2)
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.A = np.array([x1, y1])
        self.B = np.array([x2, y2])
        self.len = self.length()
        self.u = self.unit_vector()

    # Computes the length of the line segment
    def length(self):
        return la.norm(self.B - self.A)

    # Computes the unit vector of the directed line segment
    def unit_vector(self) -> np.ndarray:
        if self.length() < np.finfo(float).eps:
            u = np.array([0, 0])
        else:
            u = (self.B - self.A) / self.length()

        return u

    # Checks if the line segment has collapsed in to a point or not
    def is_degenerate(self) -> bool:
        return self.len <= np.finfo(float).eps

    # Computes the shortest distance between the line segment and the given pt 'p'
    def distance_from_pt(self, p) -> float:
        pt = np.array(p)  # convert to numpy array

        # Has the line collapsed to a point?
        if self.is_degenerate():
            # Yes, so return the distance between one of the end pts and p
            return la.norm(pt - self.A)

        # Compute projection of p on to the line segment
        proj = np.dot(pt - self.A, self.u)
        if proj > self.length() or proj < 0:
            # projection falls outside the line segment
            # so, d is simply the min distance between the ends pts and p
            d = min(la.norm(pt - self.A), la.norm(pt - self.B))
        else:
            # projection is within the line segment
            projected_pt = self.A + proj*self.u  # compute projected pt
            d = la.norm(pt - projected_pt)  # d is simply the distance between projected pt and p

        return d
