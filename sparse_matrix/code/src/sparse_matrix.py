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
                num_cols = int(lines[1].split('='))
        except Exception as e:
