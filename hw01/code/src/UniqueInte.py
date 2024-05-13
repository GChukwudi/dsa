#!/usr/bin/python3

import os
import time


class UniqueInt:
    @staticmethod
    def processFile(inputFilePath, outputFilePath):
        start_time = time.time()
        unique_integers = []

        seen = [False] * 2047

        with open(inputFilePath, 'r') as inputFile:
            for line in inputFile:
                line = line.strip()
                if line:
                    try:
                        num = int(line)
                        if -1023 <= num <= 1023 and not seen[num + 1023]:
                            unique_integers.append(num)
                            seen[num + 1023] = True

                    except ValueError:
                        pass

        UniqueInt.sorted_int(unique_integers)

        with open(outputFilePath, 'w') as outputFile:
            for num in unique_integers:
                outputFile.write(str(num) + '\n')

        end_time = time.time()
        return end_time - start_time
    
    @staticmethod
    def sorted_int(arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(current_dir, "../../sample_inputs")
    output_dir = os.path.join(current_dir, "../../sample_results")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            inputFilePath = os.path.join(input_dir, filename)
            outputFilePath = os.path.join(output_dir, filename.replace(".txt", "_result.txt"))
            runtime = UniqueInt.processFile(inputFilePath, outputFilePath)
            print(f"Processed {inputFilePath} in {runtime:.2f} seconds")