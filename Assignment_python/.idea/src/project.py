# Assignment2 (COMP348)
# Yuqian Cai (40187954)
# June 14th 2024

import json
import math
import sys
import random

# open file
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
        return data

# display menu
def display_menu():
    print("==============================================")
    print("1. Display Global Statistics")
    print("2. Display Base Station Statistics")
    print("    2.1 Statistics for a random station")
    print("    2.2 Choose a station by Id")
    print("3. Check Coverage")
    print("4. Exit")
    print("==============================================\n")

# Helper function to calculate statistics for given base stations
def calculate_statistics(base_stations, min_lat, max_lat, min_lon, max_lon, step):
    total_num_bs = len(base_stations)  # Total number of base stations
    total_num_ants = sum(len(bs['ants']) for bs in base_stations)  # Total number of antennas

    ants_per_base_station = [len(bs['ants']) for bs in base_stations]
    max_num_ants_per_bs = max(ants_per_base_station)  # Maximum number of antennas per base station
    min_num_ants_per_bs = min(ants_per_base_station)  # Minimum number of antennas per base station
    avg_num_ants_per_bs = sum(ants_per_base_station) / total_num_bs  # Average number of antennas per base station

    points_coverage = {}  # Dictionary to keep track of coverage points and corresponding antennas
    antenna_coverage_count = {}  # Dictionary to count points for each antenna

    for bs in base_stations:
        for ant in bs['ants']:
            antenna_id = (bs['id'], ant['id'])
            antenna_coverage_count[antenna_id] = 0
            for point in ant['pts']:
                point_key = tuple(point[:2])  # including lat and lon as the key, ignoring the third element
                if point_key not in points_coverage:
                    points_coverage[point_key] = []
                points_coverage[point_key].append((bs['id'], ant['id'], point[2]))  # appends a tuple containing the base station ID, antenna ID, and signal strength to the list of that point.
                antenna_coverage_count[antenna_id] += 1  # Count the points covered by this antenna

    points_covered_by_one = sum(1 for points in points_coverage.values() if len(points) == 1)  # Points covered by exactly one antenna
    points_covered_by_more = sum(1 for points in points_coverage.values() if len(points) > 1)  # Points covered by more than one antenna

    # total possible points
    total_pts =((max_lat - min_lat) / step + 1) * ((max_lon - min_lon) / step + 1)
    total_uncovered_pts = math.ceil(total_pts - len(points_coverage))# Points not covered by any antenna

    max_ants_cover_per_pt = max(len(points) for points in points_coverage.values())  # Maximum number of antennas that cover one point
    avg_ants_cover_per_pt = sum(len(points) for points in points_coverage.values()) / len(points_coverage)  # Average number of antennas covering a point

    percent_covered_area = 100 * len(points_coverage) / total_pts  # Percentage of the area covered

    # The id of the base station and antenna covering the maximum number of points
    most_covering_antenna = max(antenna_coverage_count.items(), key=lambda x: x[1])


    return {
        'total_num_bs': total_num_bs,
        'total_num_ants': total_num_ants,
        'max_num_ants_per_bs': max_num_ants_per_bs,
        'min_num_ants_per_bs': min_num_ants_per_bs,
        'avg_num_ants_per_bs': avg_num_ants_per_bs,
        'points_covered_by_one': points_covered_by_one,
        'points_covered_by_more': points_covered_by_more,
        'total_uncovered_pts': total_uncovered_pts,
        'max_ants_cover_per_pt': max_ants_cover_per_pt,
        'avg_ants_cover_per_pt': avg_ants_cover_per_pt,
        'percent_covered_area': percent_covered_area,
        'most_covering_antenna': most_covering_antenna
    }

# calculate global statistics
def global_statistics(data):
    stats = calculate_statistics(
        data['baseStations'],
        data['min_lat'], data['max_lat'],
        data['min_lon'], data['max_lon'],
        data['step']
    )

    # print
    print(f"The total number of base stations = {stats['total_num_bs']}")
    print(f"The total number of antennas = {stats['total_num_ants']}")
    print(f"The max, min and average of antennas per BS = {stats['max_num_ants_per_bs']}, {stats['min_num_ants_per_bs']}, {stats['avg_num_ants_per_bs']}")
    print(f"The total number of points covered by exactly one antenna = {stats['points_covered_by_one']}")
    print(f"The total number of points covered by more than one antenna = {stats['points_covered_by_more']}")
    print(f"The total number of points not covered by any antenna = {stats['total_uncovered_pts']}")
    print(f"The maximum number of antennas that cover one point = {stats['max_ants_cover_per_pt']}")
    print(f"The average number of antennas covering a point = {stats['avg_ants_cover_per_pt']}")
    print(f"The percentage of the covered area = {stats['percent_covered_area']:.2f}%")
    print(f"The id of the base station and antenna covering the maximum number of points = base station {stats['most_covering_antenna'][0][0]}, antenna {stats['most_covering_antenna'][0][1]} with {stats['most_covering_antenna'][1]} points covered")

# calculate base station statistics
def base_station_statistics(data, bs_id=None): #base station's id default as none
    if bs_id is None:
        bs = random.choice(data['baseStations'])
    else:
        bs = next((bs for bs in data['baseStations'] if bs['id'] == bs_id), None)

    if bs is None:
        print("Base station not found.")
        return

    stats = calculate_statistics(
        [bs],  # Pass a list containing only the selected base station
        data['min_lat'], data['max_lat'],
        data['min_lon'], data['max_lon'],
        data['step']
    )

    print(f"Statistics for base station {bs['id']}:")
    print(f"The total number of antennas = {stats['total_num_ants']}")
    print(f"The total number of points covered by exactly one antenna = {stats['points_covered_by_one']}")
    print(f"The total number of points covered by more than one antenna = {stats['points_covered_by_more']}")
    print(f"The total number of points not covered by any antenna = {stats['total_uncovered_pts']}")
    print(f"The maximum number of antennas that cover one point = {stats['max_ants_cover_per_pt']}")
    print(f"The average number of antennas covering a point = {stats['avg_ants_cover_per_pt']}")
    print(f"The percentage of the covered area by the base station = {stats['percent_covered_area']:.2f}%")
    print(f"The id of the antenna covering the maximum number of points = antenna {stats['most_covering_antenna'][0][1]} with {stats['most_covering_antenna'][1]} points covered")

# check the coverage for a specific point
def check_coverage(data, lat, lon):
    base_stations = data['baseStations']
    points_coverage = {}
    for bs in base_stations:
        for ant in bs['ants']:
            for point in ant['pts']:
                point_key = tuple(point[:2])
                if point_key not in points_coverage:
                    points_coverage[point_key] = []
                points_coverage[point_key].append((bs['id'], ant['id'], point[2]))

    # Check if the point is covered by any antenna, print all statistics from list
    if (lat, lon) in points_coverage:
        print(f"The point ({lat}, {lon}) is covered by the following base stations and antennas:")
        for bs_id, ant_id, power in points_coverage[(lat, lon)]:
            print(f"Base station {bs_id}, Antenna {ant_id}, Power {power} dBm")
    else:
        # Find the nearest antenna if the coordinate is not explicitly covered
        min_distance = float('inf') #Initialize to Infinity
        nearest_antenna = None
        for point, antennas in points_coverage.items():
            dist = ((point[0] - lat) ** 2 + (point[1] - lon) ** 2) ** 0.5 #sqrt(x^2+y^2)
            if dist < min_distance:
                min_distance = dist
                nearest_antenna = antennas[0]
                nearest_point = point

        if nearest_antenna: #if is not none
            print(f"The point ({lat}, {lon}) is not covered. Nearest antenna is at coordinates {nearest_point} with Base station {nearest_antenna[0]}, Antenna {nearest_antenna[1]} at a distance of {min_distance} units")

# main function to handle user interaction and execute commands
def main(file_path):
    data = load_json(file_path)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            global_statistics(data)
        elif choice == '2':
            sub_choice = input("1. Statistics for a random station\n2. Choose a station by Id\nEnter your choice: ")
            if sub_choice == '1':
                base_station_statistics(data)
            elif sub_choice == '2':
                bs_id = int(input("Enter the base station Id: "))
                base_station_statistics(data, bs_id)
        elif choice == '3':
            lat = float(input("Enter the latitude: "))
            lon = float(input("Enter the longitude: "))
            check_coverage(data, lat, lon)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 assignment2.py <test_file_json.json>")
        sys.exit(1)

    file_path = sys.argv[1]
    main(file_path)
