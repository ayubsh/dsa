import math
import unittest
from typing import List

def two_crystal_balls(breaks: List[bool]) -> int:
    jumpamount = math.floor(math.sqrt(len(breaks)))
    ij = jumpamount
    
    #print("outside", i)
    for i in range(jumpamount, len(breaks)):
        if breaks[i]:
            break
        i += jumpamount

    ij -= jumpamount

    for j in range(ij, len(breaks)):
        if breaks[j]:
            return j

    return -1

class TestCrystalBalls(unittest.TestCase):

    def test_random_break_point(self):
        """Standard case: ball breaks somewhere in the middle."""
        data = [False] * 1000
        break_index = 723
        for i in range(break_index, 1000):
            data[i] = True
        self.assertEqual(two_crystal_balls(data), break_index)

    def test_breaks_at_start(self):
        """Edge case: ball breaks at the very first floor."""
        data = [True, True, True]
        self.assertEqual(two_crystal_balls(data), 0)

    def test_breaks_at_end(self):
        """Edge case: ball breaks at the very last floor."""
        data = [False, False, False, True]
        self.assertEqual(two_crystal_balls(data), 3)

    def test_never_breaks(self):
        """Edge case: ball never breaks."""
        data = [False] * 100
        self.assertEqual(two_crystal_balls(data), -1)

    def test_small_array(self):
        """Edge case: very small floor count."""
        self.assertEqual(two_crystal_balls([False, True]), 1)
        self.assertEqual(two_crystal_balls([False]), -1)

if __name__ == '__main__':
    unittest.main()
