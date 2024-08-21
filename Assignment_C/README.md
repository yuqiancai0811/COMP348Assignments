# COMP 348 Assignment 1 - Search and Sort Application (C)

## Description
This project is part of the COMP 348 course, focusing on hands-on experience with the C programming language. The goal is to develop a simple search and sort application that reads words from a text file, sorts them based on user specifications, and displays the results.

### Features:
- Read text from a file and store it into an array of strings.
- Command-line interface for specifying input file, word count, word type, sort order, and optional skip words.
- Sort words in ascending or descending order.
- Support for skipping specific words during sorting.
- Option to define word types (alpha, alphanumeric, all).
- Output sorted words in a formatted way, breaking lines after every 10th word.

## Files
The project is divided into the following files:

1. **`ssort.c`**  
   Contains the `main()` function and processes command-line arguments.

2. **`fileread.c`**  
   Implements file reading logic, including the handling of skip words.

3. **`wordtype.c`**  
   Implements the logic for handling different word types (alpha, alphanumeric, all).

4. **`output.c`**  
   Contains logic related to sorting and printing the output, including error messages.

## Compilation
To compile the project, ensure all `.c` and `.h` files are in the same directory. Use the following GCC command:

```bash
gcc –Wall ssort.c fileread.c wordtype.c output.c -o ssort
