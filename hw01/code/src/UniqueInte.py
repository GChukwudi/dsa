#!/usr/bin/python3

import os
import time


class UniqueInt:
    """
    A class that processes a file containing integers and writes unique integers within a specific range to an output file.
    """
    @staticmethod
    def processFile(inputFilePath, outputFilePath):
        """
        Processes the input file and writes unique integers within the range [-1023, 1023] to the output file.

        Args:
            inputFilePath (str): The path to the input file.
            outputFilepath (str): The path to the output file.

        return float: The time taken to process the file in seconds.
        """
        start_time = time.time()
        unique_integers = []

        seen = [False] * 2047

        # Read the input file and store unique integers within the range [-1023, 1023]
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

        # Sort the unique integers in ascending order
        UniqueInt.sorted_int(unique_integers)

        # Write the unique integers to the output file
        with open(outputFilePath, 'w') as outputFile:
            for num in unique_integers:
                outputFile.write(str(num) + '\n')

        end_time = time.time()
        return end_time - start_time
    
    # Sorts the array in ascending order using the insertion sort algorithm.
    @staticmethod
    def sorted_int(arr):
        """
        Sorts the array in ascending order using the insertion sort algorithm.

        Args: 
            arr (list): The list of integers to be sorted.
        """
        for i in range(1, len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key


if __name__ == "__main__":
    # Process all input files in the sample_inputs directory and write the results to the sample_results directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(current_dir, "../../sample_inputs")
    output_dir = os.path.join(current_dir, "../../sample_results")

    # Create the output directory if it does not exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Process each input file in the input directory
    for filename in os.listdir(input_dir):
        if filename.endswith(".txt"):
            inputFilePath = os.path.join(input_dir, filename)
            outputFilePath = os.path.join(output_dir, filename.replace(".txt", "_result.txt"))
            runtime = UniqueInt.processFile(inputFilePath, outputFilePath)
            print(f"Processed {inputFilePath} in {runtime:.2f} seconds")
