from flask import Flask, request

app = Flask(__name__)


def check_constraints(matrix):
    if type(matrix) is not list:
        return {'error': 'Input must be a list'}, 400, None, None

    if len(matrix) == 0:
        return {'error': 'Input cannot be an empty list'}, 400, None, None

    if all(isinstance(i, list) for i in matrix):
        if not all(len(i) == len(matrix[0]) for i in matrix):
            return {'error': 'Input must be a vector or matrix'}, 400, None, None

    if type(matrix[0]) is not list:
        m = 1
        n = len(matrix)
    else:
        m = len(matrix)
        n = len(matrix[0])

    if not (1 <= m <= 1000):
        return {'error': 'Number of rows must be between 1 and 1000'}, 400, m, n

    if not (1 <= n <= 1000):
        return {'error': 'Number of columns must be between 1 and 1000'}, 400, m, n

    if not (m * n <= 105):
        return {'error': 'Number of values must be less than or equal to 105'}, 400, m, n

    if type(matrix[0]) is not list:
        for value in matrix:
            if type(value) not in [int, float]:
                return {'error': 'Values must be numeric'}, 400, m, n
            if not (-109 <= value <= 109):
                return {'error': 'Values must be between -109 and 109'}, 400, m, n

    return None, 200, m, n


@app.route('/transpose', methods=['POST'])
def transpose(matrix=None):

    if matrix is None:
        matrix = request.get_json()

    error, status, m, n = check_constraints(matrix)
    if error:
        return error

    transposed = []
    if type(matrix[0]) is not list:
        transposed = [[value] for value in matrix]
    else:
        for j in range(n):
            row = []
            for i in range(m):
                row.append(matrix[i][j])
            transposed.append(row)

    return transposed, 200
