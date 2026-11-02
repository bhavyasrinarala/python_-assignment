

import math

# Create an empty list for coordinates
locations = []

n = int(input("Enter number of locations: "))

# Read geographical coordinates
for i in range(n):
    print("\nLocation", i + 1)

    latitude = float(input("Enter latitude: "))
    longitude = float(input("Enter longitude: "))

    locations.append((latitude, longitude))

longest = 0
longest_route = None

print("\n----- ROUTE DISTANCE ANALYSIS -----")

# Calculate distances between successive locations
for i in range(n - 1):

    x1, y1 = locations[i]
    x2, y2 = locations[i + 1]

    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print("Route", i + 1, "to", i + 2,
          "Distance:", round(distance, 2))

    if distance > longest:
        longest = distance
        longest_route = (i + 1, i + 2)

# Display longest route
print("\nLongest Route Segment:", longest_route)
print("Longest Distance:", round(longest, 2))
