# !/usr/bin/python3

import sys
from collections import defaultdict


class SparseMatrix:
    def __init__(self, matrixFilePath):
        self.matrix = defaultdict(int)
        self.rows = 0
        self.cols = 0
        self.matrix = defaultdict(int)
        if matrixFilePath:
            self.read_matrix(matrixFilePath)

    def read_matrix(self, matrixFilePath):
        try:
            with open(matrixFilePath, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    line = line.strip()
                    if 'rows=' in line:
                        self.rows = int(line.split('=')[1].strip())
                    elif 'cols=' in line:
                        self.cols = int(line.split('=')[1].strip())
                    elif line:
                        if not (line.startswith('(') and line.endswith(')')):
                            raise ValueError("Input file has wrong format")
                        try:
                            row, col, val = map(int, line[1:-1].split(','))
                            self.matrix[(row, col)] = val
                        except ValueError:
                            raise ValueError("Input file has wrong format")
        except FileNotFoundError:
            raise FileNotFoundError(f"File {matrixFilePath} not found")
        except ValueError as e:
            raise ValueError(f"Error reading file: {e}")
        
    def getElement(self, currRow, currCol):
        return self.matrix.get((currRow, currCol), 0)
    
    def setElement(self, currRow, currCol, value):
        if value != 0:
            self.matrix[(currRow, currCol)] = value
        elif (currRow, currCol) in self.matrix:
            del self.matrix[(currRow, currCol)]

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices have different dimensions")
        result = SparseMatrix(None)
        result.rows = self.rows
        result.cols = self.cols
        result.matrix = self.matrix.copy()
        for (row, col), value in other.matrix.items():
            result.setElement(row, col, result.getElement(row, col) + value)
        return result
    
    def subtract(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrices have different dimensions")
        result = SparseMatrix(None)
        result.rows = self.rows
        result.cols = self.cols
        result.matrix = self.matrix.copy()
        for (row, col), value in other.matrix.items():
            result.setElement(row, col, result.getElement(row, col) - value)
        return result
    
    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Number of columns in the first matrix must be equal to the number of rows in the second matrix")
        result = SparseMatrix(None)
        result.rows = self.rows
        result.cols = other.cols
        for (row1, col1), value1 in self.matrix.items():
            for col2 in range(other.cols):
                value2 = other.getElement(col1, col2)
                if value2 != 0:
                    result.setElement(row1, col2, result.getElement(row1, col2) + value1 * value2)
        return result
    
    def print_matrix(self):
        for (row, col), value in self.matrix.items():
            print(f"({row}, {col}, {value})")

def main():
    if len(sys.argv) != 4:
        print("Usage: python3 sparse_matrix.py <operation> <matrix1> <matrix2>")
        sys.exit(1)
    operation = sys.argv[1]
    matrix1 = sys.argv[2]
    matrix2 = sys.argv[3]

    try:
        matrixA = SparseMatrix(matrix1)
        matrixB = SparseMatrix(matrix2)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

    if operation == 'add':
        result = matrixA.add(matrixB)
    elif operation == 'subtract':
        result = matrixA.subtract(matrixB)
    elif operation == 'multiply':
        result = matrixA.multiply(matrixB)
    else:
        print("Invalid operation")
        sys.exit(1)

    result_file = "result.txt"
    with open(result_file, 'w') as file:
        file.write(f"rows={result.rows}\n")
        file.write(f"cols={result.cols}\n")
        for (row, col), value in result.matrix.items():
            file.write(f"({row}, {col}, {value})\n")

    print(f"Result written to {result_file}")


if __name__ == "__main__":
    main()