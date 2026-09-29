import unittest
from grade_utils import calculate_percentage, get_grade_info, is_pass

class TestGradeUtils(unittest.TestCase):
    def test_percentage(self):
        self.assertEqual(calculate_percentage(45,50),90)

    def test_grade_boundaries(self):
        self.assertEqual(get_grade_info(90),("A+",10))
        self.assertEqual(get_grade_info(80),("A",9))
        self.assertEqual(get_grade_info(39),("F",0))

    def test_pass(self):
        self.assertTrue(is_pass(40))
        self.assertFalse(is_pass(39))

if __name__=="__main__":
    unittest.main()
