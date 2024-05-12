#!/usr/bin/python3

import os
import time


class UniqueInt:
    @staticmethod
    def processFile(inputFilePath, outputFilePath):
        start_time = time.time()
        unique_integers = set()
        with open(inputFilePath, 'r') as inputFile:
            for line in inputFile:
                line = line.strip()
                if line:
                    try:
                        num = int(line)
                        if -1023 <= num <= 1023:
                            unique_integers.add(num)
                    except ValueError:
                        pass

        with open(outputFilePath, 'w') as outputFile:
            for num in sorted(unique_integers):
                outputFile.write(str(num) + '\n')

        end_time = time.time()
        return end_time - start_time
# import sys

# class UniqueInt:
#     @staticmethod
#     def processFile(inputFilePath, outputFilePath):
#         unique_integers = set()
#         with open(inputFilePath, 'r') as inputFile:
#             for line in inputFile:
#                 line = line.strip()
#                 if line:
#                     try:
#                         num = int(line)
#                         if -1023 <= num <= 1023:
#                             unique_integers.add(num)
#                     except ValueError:
#                         pass

#         with open(outputFilePath, 'w') as outputFile:
#             for num in sorted(unique_integers):
#                 outputFile.write(str(num) + '\n')

# if __name__ == "__main__":
#     input_dir = "/dsa/hw01/sample_inputs"
#     output_dir = "/dsa/hw01/sample_outputs"

#     for filename in os.listdir(input_dir):
#         if filename.endswith(".txt"):
#             inputFilePath = os.path.join(input_dir, filename)
#             outputFilePath = os.path.join(output_dir, filename.replace(".txt", "_output.txt"))
#             UniqueInt.processFile(inputFilePath, outputFilePath)
