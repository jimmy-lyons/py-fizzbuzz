import unittest

from fizzbuzz import generate

class TestFizzbuzz(unittest.TestCase):  
  def test_lists_values_up_to_one(self): 
    self.assertEqual(generate(1), "1")  

  def test_lists_values_up_to_two(self): 
    self.assertEqual(generate(2), "1, 2")

  def test_lists_values_up_to_three(self): 
    self.assertEqual(generate(3), "1, 2, fizz")

  def test_lists_values_up_to_four(self): 
    self.assertEqual(generate(4), "1, 2, fizz, 4")

  def test_lists_values_up_to_five(self): 
    self.assertEqual(generate(5), "1, 2, fizz, 4, buzz")
