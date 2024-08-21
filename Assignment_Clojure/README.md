# COMP 348 Assignment 3 - City Information System (Clojure)

## Overview
This project is a simple information system developed in Clojure that loads data from a file and allows the user to interact with it through a menu-driven interface. The system manages a database of cities, including details such as city name, province, size, population, and area. The user can perform various queries and retrieve statistics based on this data.

## Features
The program provides the following options to the user:

1. **List Cities**
   - 1.1. List all cities ordered by city name (ascending).
   - 1.2. List all cities for a specific province, ordered by size (descending) and city name (ascending).
   - 1.3. List all cities for a specific province, ordered by population density (ascending).

2. **Display City Information**
   - Allows the user to input a city name and returns detailed information about the city.

3. **List Provinces**
   - Lists all provinces with the total number of cities on file, ordered by the number of cities in each province.

4. **Display Province Information**
   - Lists all provinces along with their total population, ordered by province name.

5. **Exit**
   - Exits the program with a "Good Bye" message.

## File Structure
- **`app.clj`**: The main file that loads city data into data structures and passes it to the menu for further interaction.
- **`menu.clj`**: Implements the user interface and handles user input to navigate through different options in the program.
- **`db.clj`**: Contains data management logic, such as loading and organizing city data from the input file.

## Installation
### Prerequisites:
- Ensure you have Clojure installed on your machine. You can find installation instructions [here](https://clojure.org/guides/getting_started).

### Running the Program:
1. **Set the Classpath**:
   - Before running the program, ensure that the current directory is included in your `CLASSPATH`:
     ```bash
     export CLASSPATH=./
     ```

2. **Run the Program**:
   - From the command line, execute the main file:
     ```bash
     clojure app.clj
     ```