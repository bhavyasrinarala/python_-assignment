
registrations = []

n = int(input("Enter number of registrations: "))

# Read registration details
for i in range(n):
    print("\nRegistration", i + 1)

    sid = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    course = input("Enter Course Name: ").strip().title()

    registrations.append((sid, name, course))

# Identify duplicate registrations
duplicates = []

for i in range(len(registrations)):
    for j in range(i):
        if (registrations[i][0] == registrations[j][0]
                and registrations[i][2] == registrations[j][2]):
            duplicates.append(i)
            break

# Group courses by student
student_courses = {}

for sid, name, course in registrations:
    if sid not in student_courses:
        student_courses[sid] = []
    if course not in student_courses[sid]:
        student_courses[sid].append(course)

# Validate registrations
valid = []
invalid = []

for i in range(len(registrations)):
    sid, name, course = registrations[i]
    reasons = []

    if i in duplicates:
        reasons.append("Duplicate Registration")

    courses = student_courses[sid]

    if len(courses) > 3:
        reasons.append("More than 3 Courses")

    if "Python" in courses and "Java" in courses:
        reasons.append("Invalid Course Combination")

    if reasons:
        invalid.append((sid, name, course, reasons))
    else:
        valid.append(registrations[i])

# Display results
print("\n----- VALID REGISTRATIONS -----")

for item in valid:
    print(item)

print("\n----- INVALID REGISTRATIONS -----")

for item in invalid:
    print(item[0], item[1], item[2], "-", ", ".join(item[3]))

# Display students who violated rules
print("\n----- STUDENTS VIOLATING RULES -----")

violators = []

for item in invalid:
    if item[0] not in violators:
        violators.append(item[0])
        print(item[0], "-", item[1])

