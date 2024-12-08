import sys
import unittest

sys.path.insert(1, '../figures')

from circle import area as c_area
from rectangle import area as r_area
from square import area as s_area
from triangle import area as t_area


class TestArea(unittest.TestCase):
    '''
        Тест работы метода area() для каждой фигуры

        tests = [] - массив входных данных
        test_results = [] - массив значений для сравнения
    '''

    def test_circle(self):
        tests = [0, 1, 3, -4, 1548, 4.5]
        tests_results = [0, 3.14, 28.27, -1, 7528211.04, 63.62]

        for i in range(len(tests)):
            self.assertAlmostEqual(c_area(tests[i]), tests_results[i], places=2)

    def test_rectangle(self):
        tests = [(0, 0), (-5, -3), (-5, 4), (0, -6), (1, 1),
                 (3, 5), (0.34, 0.6), (5478, 3306)]
        tests_results = [0, -1, -1, -1, 1, 15, 0.204, 18110268]

        for i in range(len(tests)):
            self.assertAlmostEqual(r_area(*tests[i]), tests_results[i])

    def test_square(self):
        tests = [1, 0, -4, -345, 4, 3.5, 100500]
        tests_results = [1, 0, -1, -1, 16, 12.25, 10100250000]

        for i in range(len(tests)):
            self.assertAlmostEqual(s_area(tests[i]), tests_results[i])

    def test_triangle(self):
        tests = [(0, 0), (-5, -3), (-5, 4), (0, -6), (1, 1),
                 (3, 5), (0.34, 0.6), (5478, 3306)]
        tests_results = [0, -1, -1, -1, 0.5, 7.5, 0.102, 9055134]

        for i in range(len(tests)):
            self.assertAlmostEqual(t_area(*tests[i]), tests_results[i])
