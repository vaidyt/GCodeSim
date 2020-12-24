import numpy as np
from numpy import linalg as la


class LineSeg2D:

    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        self.A = np.array([x1, y1])
        self.B = np.array([x2, y2])
        self.len = self.length()
        self.u = self.unit_vector()

    def length(self):
        return la.norm(self.B - self.A)

    def unit_vector(self):
        if self.length() < np.finfo(float).eps:
            u = np.array([0, 0])
        else:
            u = (self.B - self.A) / self.length()

        return u

    def is_degenerate(self) -> bool:
        return self.len <= np.finfo(float).eps

    def distance_from_pt(self, p) -> float:
        pt = np.array(p)  # convert to numpy array

        # Has line collapsed to a point?
        if self.is_degenerate():
            # Yes, so return the distance between one of the end pts and p
            return la.norm(pt - self.A)

        # We have a generic line segment
        ap = pt - self.A
        # Project p on to the line segment and compute the projection
        proj = np.dot(ap, self.u)
        if proj > self.length() or proj < 0:
            # projection falls outside the line segment
            # so, d is simply the min distance between the ends pts and p
            d = min(la.norm(self.A - pt), la.norm(self.B - pt))
        else:
            # projection is within the line segment
            projected_pt = self.A + proj*self.u  # compute projected pt
            d = la.norm(projected_pt - pt)  # d is simply the distance between projected pt and p

        return d
