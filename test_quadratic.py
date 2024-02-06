"""Template for Lesson 08 In-Class Exercise on testing"""

from quadratic import quadratic_roots
import unittest

class TestQuadratic(unittest.TestCase):

    def test_no_roots(self):
        """check that an empty list is returned when no solution"""
        roots = quadratic_roots(1., 0., 1.)
        self.assertTrue(len(roots)==0)

    def test_one_root(self):
        """test when quadratic has only one solution"""
        # Add your test here
        roots = quadratic_roots(1., 2., 1.)
        self.assertTrue(len(roots)==1)
        self.assertAlmostEqual(roots[0], -1.0, places=12);
        
    def test_two_roots(self):
        """test when quadratic has two solutions"""
        # Add your test here
        roots = quadratic_roots(1., 5., 4.);
        self.assertTrue(len(roots)==2)
        self.assertAlmostEqual( min(roots), -4.0, places=12);
        self.assertAlmostEqual(max(roots), -1.0, places=12);

if __name__ == '__main__':
    unittest.main()
