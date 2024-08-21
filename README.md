# COMP 348 Assignment Summary

This repository contains three assignments for COMP 348, each exploring different programming paradigms through hands-on projects in C, Python, and Clojure.

## Assignment 1 - Search and Sort Application (C)
A simple C-based search and sort program reads words from a text file, sorts them based on user input, and displays the results.

- **Key Features**: Command-line interface, support for word types (alpha, alphanumeric, all), sorting (ascending/descending), and skip words.
- **Files**: 
  - `ssort.c`: Main function and command-line argument handling.
  - `fileread.c`: File reading and skip word logic.
  - `wordtype.c`: Word type handling.
  - `output.c`: Sorting and output formatting.
- **Compilation**: Run `gcc -Wall ssort.c fileread.c wordtype.c output.c -o ssort`.

## Assignment 2 - Cellular Network Coverage Analysis (Python)
A Python program that processes a JSON file representing a cellular network's coverage, displaying global and base station-specific statistics.

- **Key Features**: Menu interface for global stats, base station stats, and coverage checks for specific coordinates.
- **File**: 
  - `assignment2.py`: Handles JSON processing and user interaction.
- **Execution**: Run `python3 assignment2.py <test_file.json>`.

## Assignment 3 - City Information System (Clojure)
A functional programming project in Clojure that manages city data and allows users to interact via a menu to retrieve city and province statistics.

- **Key Features**: List cities, city info, province stats, and population data using functional programming techniques (`map`, `reduce`, `filter`).
- **Files**: 
  - `app.clj`: Main program flow.
  - `menu.clj`: User interface and menu logic.
  - `db.clj`: Data loading and processing.
- **Execution**: Set the CLASSPATH (`export CLASSPATH=./`), then run `clojure app.clj`.

---

These assignments provide a broad exposure to structured, procedural, and functional programming through practical applications.
