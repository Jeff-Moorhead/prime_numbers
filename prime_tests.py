"""Tests for prime_functions.py"""
import unittest
import prime_functions as pf

class PrimeTest(unittest.TestCase):

    def test_is_factor(self):
        """Test the is_factor function."""
        factor = pf.is_factor(99, 3)
        self.assertTrue(factor)

    def test_is_not_factor(self):
        """Test the is factor function for the case where fact is not
        a factor of num"""
        not_factor = pf.is_factor(99, 4)
        self.assertFalse(not_factor)

    def test_prime(self):
        """Check if an prime argument returns True."""
        prime_num = pf.is_prime(23)
        # Check that prime is True
        self.assertTrue(prime_num)

    def test_comp(self):
        """Test if a composite number returns False"""
        comp_num = pf.is_prime(99)
        self.assertFalse(comp_num)

    def test_pfs(self):
        """Test the find_pfs function."""
        pfs = [2, 5, 3]
        prime_factors = pf.find_pfs(30)
        for factor in pfs:
            self.assertIn(factor, prime_factors)

    def test_check_factors(self):
        """Test the check_factors function."""
        pfs = [2, 3, 5]
        prime_factors = pf.find_pfs(30)
        self.assertEqual(prime_factors, pfs)

unittest.main()
