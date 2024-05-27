#!/usr/bin/python3

import os
from collections import defaultdict


class SparseMatrix:
    def __init__(self, file_path=None, num_rows=None, num_cols=None):
        if file_path:
            self.num_rows, self.num_cols, self.elements = self.read_from_file(file_path)
        elif num_rows is not None and num_cols is not None:
            self.num_rows = num_rows
            self.num_cols = num_cols
            self.elements = defaultdict(int)
        else:
            raise ValueError("Invalid arguments")
        
        
    def _read_from_file(self, file_path):
        elements = defaultdict(int)
        try:
            with open(file_path, 'r') as file:
                lines = file.readlines()
                num_rows = int(lines[0].split('=')[1].strip())
                num_cols = int(lines[1].split('='))[1].strip()

                for line in lines[2:]:
                    line = line.strip()
                    if not line:
                        continue
                    if not (line.startswith('(') and line.endswith(')')):
                        raise ValueError("Invalid file format")
                    try:
                        row, col, value = map(int, line[1:-1].split(','))
                        elements[(row, col)] = value
                    except ValueError:
                        raise ValueError("Invalid file format")
        except Exception as e:
            raise ValueError(f"Error reading file: {e}")

        return num_rows, num_cols, elements
    
    def get_element(self, row, col):
        return self.elements.get((row, col), 0)
    
    def set_element(self, row, col, values):
        if values != 0:
            self.elements[(row, col)] = values
        elif (row, col) in self.elements:
            del self.elements[(row, col)]

    def add(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        result.elements = self.elements.copy()
        for (row, col), values in other.elements.items():
            result.set_element(row, col, result.get_element(row, col) + values)
        return result
    
    def multiply(self, other):
        if self.num_cols != other.num_rows:
            raise ValueError("Matrix dimensions do not match")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=other.num_cols)
        for (row, col), values in self.elements.items():
            for i in range(other.num_cols):
                result.set_element(row, i, result.get_element(row, i) + values * other.get_element(col, i))
        return result

    def subtract(self, other):
        if self.num_rows != other.num_rows or self.num_cols != other.num_cols:
            raise ValueError("Matrix dimensions do not match")
        result = SparseMatrix(num_rows=self.num_rows, num_cols=self.num_cols)
        result.elements = self.elements.copy()
        for (row, col), values in other.elements.items():
            result.set_element(row, col, result.get_element(row, col) - values)
        return result
    
def main():
    import sys
    if len(sys.argv) != 4:
        print("Usage: python3 sparse_matrix.py <operation> <input_file1> <input_file2>")
        # print("Usage: python3 sparse_matrix.py <input_file1> <input_file2>")
        sys.exit(1)

        # operation = sys.argv[3]
        # input_file1 = sys.argv[1]
        # input_file2 = sys.argv[2]
        operation = sys.argv[1]
        input_file1 = sys.argv[2]
        input_file2 = sys.argv[3]

        try:
            matrix1 = SparseMatrix(file_path=input_file1)
            matrix2 = SparseMatrix(file_path=input_file2)
        except ValueError as e:
            print(e)
            sys.exit(1)

        if operation == 'add':
            result = matrix1.add(matrix2)
        elif operation == 'subtract':
            result = matrix1.subtract(matrix2)
        elif operation == 'multiply':
            result = matrix1.multiply(matrix2)
        else:
            print("Invalid operation")
            sys.exit(1)

        result_file = 'result.txt'
        with open(result_file, 'w') as file:
            file.write(f"num_rows={result.num_rows}\n")
            file.write(f"num_cols={result.num_cols}\n")
            for (row, col), values in result.elements.items():
                file.write(f"({row}, {col}, {values})\n")

        print(f"Result written to {result_file}")


if __name__ == '__main__':
    main()