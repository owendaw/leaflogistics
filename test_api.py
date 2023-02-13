import unittest
from api import transpose


class TransposeMatrixTestCase(unittest.TestCase):
    def test_valid_matrix(self):
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        expected = ([[1, 4, 7], [2, 5, 8], [3, 6, 9]], 200)
        self.assertEqual(transpose(matrix), expected)

    def test_valid_vector(self):
        vector = [1, 2, 3]
        expected = ([[1], [2], [3]], 200)
        self.assertEqual(transpose(vector), expected)

    def test_empty_matrix(self):
        matrix = []
        expected = {'error': 'Input cannot be an empty list'}
        self.assertEqual(transpose(matrix), expected)

    def test_invalid_input(self):
        invalid_input = "not a matrix"
        expected = {'error': 'Input must be a list'}
        self.assertEqual(transpose(invalid_input), expected)

    def test_matrix_with_different_number_of_columns(self):
        matrix = [[1, 2], [3, 4, 5]]
        expected = {'error': 'Input must be a vector or matrix'}
        self.assertEqual(transpose(matrix), expected)


if __name__ == "__main__":
    unittest.main()
