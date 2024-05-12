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
            outputFilePath (str): The path to the output file.

        Returns:
            float: The time taken to process the file in seconds.
        """
        # Start the timer
        start_time = time.time()
        # Read the input file and store unique integers within the range [-1023, 1023]
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

        # Write the unique integers to the output file
        with open(outputFilePath, 'w') as outputFile:
            for num in sorted(unique_integers):
                outputFile.write(str(num) + '\n')

        # End the timer
        end_time = time.time()
        return end_time - start_time

    
if __name__ == "__main__":
    # Process all input files in the sample_inputs directory and write the results to the sample_results directory
    current_dir = os.path.dirname(os.path.abspath(__file__))

    input_dir = os.path.join(current_dir, "../../sample_inputs")
    output_dir = os.path.join(current_dir, "../../sample_results")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        # Process only .txt files
        if filename.endswith(".txt"):
            inputFilePath = os.path.join(input_dir, filename)
            outputFilePath = os.path.join(output_dir, filename.replace(".txt", "_result.txt"))
            runtime = UniqueInt.processFile(inputFilePath, outputFilePath)
            print(f"Processed {filename} in {runtime:.2f} seconds.")
