import unittest
from math_quiz import get_int, get_operator, calc_problem


class TestMathGame(unittest.TestCase):

    def test_get_int(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for i in range(1000):  # Test a large number of random values
            rand_num = get_int(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_get_operator(self):
        operators = ['+', '-', '*']
        solutions = []
        for i in range(1000):
            solution = get_operator()
            # test if valid operator has been returned
            self.assertTrue(solution in operators)
            solutions.append(solution)
        # test if al valid operators have been used, make sure it is not the same every time
        self.assertTrue(set(operators).issubset(solutions))      

    def test_calc_problem(self):
            test_cases = [
                (5, 2, '+', '5 + 2', 7),
                (5, 2, '-', '5 - 2', 3),
                (5, 2, '*', '5 * 2', 10),
                (5, 7, '-', '5 - 7', -2),
            ]
            test_errors = [
                 (5, 2, '/')
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = calc_problem(num1, num2, operator)
                self.assertTrue(expected_answer == answer)
                self.assertTrue(expected_problem == problem)
            for num1, num2, operator in test_errors:
                 with self.assertRaises(ValueError):
                      calc_problem(num1, num2, operator)

if __name__ == "__main__":
    unittest.main()
