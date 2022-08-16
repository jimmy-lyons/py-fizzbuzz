import unittest

from fizzbuzz import generate

class TestFizzbuzz(unittest.TestCase):  
  def test_lists_values_up_to_one(self): 
    self.assertEqual(generate(1), "1")  

  def test_lists_values_up_to_two(self): 
    self.assertEqual(generate(2), "1, 2")

