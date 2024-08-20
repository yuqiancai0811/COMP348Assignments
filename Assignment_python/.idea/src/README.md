# Python project: Cellular Network Coverage Analyzer

## Overview
This Python program analyzes the coverage of a cellular network provider based on the data provided in a JSON file. The JSON file contains information about base stations, antennas, and the geographical points they cover. The program offers various options for displaying global and station-specific statistics, as well as checking coverage for specific coordinates.

## Features
- **Global Statistics**: Provides statistics such as the number of base stations, antennas, coverage area, and more.
- **Base Station Statistics**: Offers detailed information about individual base stations and their coverage.
- **Coverage Check**: Allows users to input coordinates and determine whether the point is covered, as well as information about the nearest antenna if not explicitly covered.

## Usage
### Command Line Execution
Run the program from the command line by providing the JSON file as an input argument:

```bash
python3 project.py <test_file.json>
