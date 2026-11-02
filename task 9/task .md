# Problem Statement
Develop a Python program to store geographical coordinates as tuples and calculate distances between successive locations using a supplied distance formula. Identify the longest route segment and display the distance between each pair of locations along with the longest segment.
# Assumptions
1. Each geographical location is represented as a tuple (latitude, longitude).
2. Coordinates are entered by the user.
3. At least two geographical locations are required.
4. The Euclidean distance formula is used for this program.
5. Distance is calculated between successive locations.
6. The longest distance is identified using the calculated values.
7. The distance is expressed in coordinate units.
Distance formula:
\[
D = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2}
\]

# Algorithm
1. Start.
2. Read the number of geographical locations.
3. Create an empty list to store coordinate tuples.
4. Read latitude and longitude for each location.
5. Store each coordinate as a tuple.
6. Initialize the longest distance as zero.
7. Use a loop to select successive coordinate pairs.
8. Calculate the distance using the supplied formula.
9. Display the distance between each successive pair.
10. Compare each distance with the longest distance.
11. Update the longest distance and route segment if necessary.
  # mermaid flow chart
  ```mermaid

flowchart TD
    A([Start]) --> B[/Enter Number of Locations/]
    B --> C[Create Empty Coordinate List]
    C --> D[/Enter Latitude and Longitude/]
    D --> E[Store Coordinates as Tuples]
    E --> F{More Locations?}
    F -->|Yes| D
    F -->|No| G[Initialize Longest Distance = 0]
    G --> H[Select Two Successive Locations]
    H --> I[Calculate Distance Using Formula]
    I --> J[Display Route Distance]
    J --> K{Distance > Longest Distance?}
    K -->|Yes| L[Update Longest Distance and Route]
    K -->|No| M[Move to Next Route]
    L --> M
    M --> N{More Route Segments?}
    N -->|Yes| H
    N -->|No| O[Display Longest Route Segment]
    O --> P([Stop])
```
# sample input

Enter number of locations: 4

Location 1
Enter latitude: 10
Enter longitude: 20

Location 2
Enter latitude: 13
Enter longitude: 24

Location 3
Enter latitude: 18
Enter longitude: 30

Location 4
Enter latitude: 20
Enter longitude: 33
13. Display the longest route segment and its distance.
14. Stop
