# COMP 348 Assignment 2 - Cellular Network Coverage Analysis (Python)

## Overview
This project is a Python-based program that reads data from a JSON file representing the coverage of a cellular network provider. The program processes the data to calculate various statistics related to base stations and antennas, and allows the user to interact with the data through a simple menu-driven interface.

## Features
Upon running the program, the user is presented with the following options:
1. **Display Global Statistics**: 
   - Shows statistics such as the total number of base stations, antennas, coverage percentage, and more.
   
2. **Display Base Station Statistics**:
   - 2.1: Provides statistics for a randomly chosen base station.
   - 2.2: Allows the user to choose a base station by its ID and view detailed statistics.

3. **Check Coverage**: 
   - Allows the user to input specific coordinates (latitude and longitude) and checks if the point is covered by any base station. If not, the nearest base station is displayed.

4. **Exit**: 
   - Exits the program with a "Good Bye" message.

## Installation
### Prerequisites:
- **Python 3.x**: Ensure Python 3 is installed on your system.
- **JSON file**: The program requires a properly formatted JSON file representing the cellular network coverage.

### Running the Program:
1. Clone the repository to your local machine.
2. Open a terminal and navigate to the project directory.
3. Run the program with the following command:
   ```bash
   python3 assignment2.py <test_file.json>
