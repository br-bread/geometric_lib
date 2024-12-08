import sys
import unittest

sys.path.insert(1, '../figures')

from circle import perimeter as c_perimeter
from rectangle import perimeter as r_perimeter
from square import perimeter as s_perimeter
from triangle import perimeter as t_perimeter


class TestPerimeter(unittest.TestCase):
    '''
        Тест работы метода perimeter() для каждой фигуры

        tests = [] - массив входных данных
        test_results = [] - массив значений для сравнения
    '''

    def test_circle(self):
        tests = [0, 1, 3, -4, 1548, 4.5]
        tests_results = [0, 6.28, 18.85, -1, 9726.37, 28.27]

        for i in range(len(tests)):
            self.assertAlmostEqual(c_perimeter(tests[i]), tests_results[i], places=2)

    def test_rectangle(self):
        tests = [(0, 0), (-5, -3), (-5, 4), (0, -6), (1, 1),
                 (3, 5), (0.34, 0.6), (5478, 3306)]
        tests_results = [0, -1, -1, -1, 4, 16, 1.88, 17568]

        for i in range(len(tests)):
            self.assertAlmostEqual(r_perimeter(*tests[i]), tests_results[i])

    def test_square(self):
        tests = [1, 0, -4, -345, 4, 3.5, 100500]
        tests_results = [4, 0, -1, -1, 16, 14, 402000]

        for i in range(len(tests)):
            self.assertAlmostEqual(s_perimeter(tests[i]), tests_results[i])

    def test_triangle(self):
        tests = [(0, 0, 0), (-1, -5, -3), (-5, 0, 3), (0, 6, 5), (1, 1, 1),
                 (3, 5, 7), (0.34, 0.6, 0.3), (5078, 3306, 1987)]
        tests_results = [0, -1, -1, -1, 3, 15, 1.24, 10371]

        for i in range(len(tests)):
            self.assertAlmostEqual(t_perimeter(*tests[i]), tests_results[i])
