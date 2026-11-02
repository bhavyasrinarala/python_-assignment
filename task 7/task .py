
rows = 5
cols = 6

capacity = rows * cols

reserved = {(1, 3), (3, 4)}

students = int(input("Enter number of students: "))

# Calculate available alternate seats
available = []

for i in range(1, rows + 1):
    for j in range(1, cols + 1):

        if (i, j) not in reserved and (i + j) % 2 == 0:
            available.append((i, j))

if students > len(available):
    print("Not enough seats available!")
else:
    seat_no = 1

    print("\nEXAMINATION SEATING ARRANGEMENT")
    print("--------------------------------")

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):

            if (i, j) in reserved:
                print(" R ", end=" ")

            elif (i + j) % 2 != 0:
                print(" X ", end=" ")

            elif seat_no <= students:
                print("S" + str(seat_no), end=" ")
                seat_no += 1

            else:
                print(" - ", end=" ")

        print()

    print("\nTotal Classroom Capacity:", capacity)
    print("Number of Students:", students)
    print("Students Seated:", seat_no - 1)
    print("Reserved Seats:", len(reserved))
    print("Alternate Seating: Enabled")

