# Data Structures and Algorithms

## Task Description
- Read a file that has one integer on each line. The integer can be positive or negative.
- For each input file in the sample folder, generate a result file containing a list of unique integers in the input file.
- Sort the integers in the result file in increasing order.
- Handle variations in the input file format, including whitespace, empty lines, lines with multiple integers, and non-integer inputs.
- The program should record runtime for each input file processed.

## File Organization
- **/dsa/hw01/code/src/**: Contains the source code for the program.
- **/dsa/hw01/sample_inputs/**: Contains sample input files for testing the program.
- **/dsa/hw01/sample_results/**: Output directory for the generated result files.

## Implementation Details
- The program is implemented in Python.
- The main logic is encapsulated in the `UniqueInt` class.
- The `processFile` method reads the input file, identifies unique integers, sorts them, and writes them to the output file.
- The program handles various input file variations as specified in the assignment.
- Runtime for each file processing is recorded and printed to the console.

## Running the Program
1. Ensure Python is installed on your system.
2. Place the input files in the `sample_inputs` directory.
3. Run the `UniqueInt.py` script located in the `src` directory.
4. Check the `sample_results` directory for the generated output files.

## Author
- God'sFavour Chukwudi