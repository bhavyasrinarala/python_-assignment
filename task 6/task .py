
applicants = []

n = int(input("Enter number of applicants: "))

course = input("Enter course (CSE/ECE/Mechanical): ").upper()

# Course eligibility criteria
if course == "CSE":
    threshold = 75
elif course == "ECE":
    threshold = 70
elif course == "MECHANICAL":
    threshold = 65
else:
    print("Invalid course")
    exit()

for i in range(n):
    print("\nEnter Candidate Details")

    cid = int(input("Candidate ID: "))
    name = input("Candidate Name: ")

    math = float(input("Mathematics Marks: "))
    physics = float(input("Physics Marks: "))
    chemistry = float(input("Chemistry Marks: "))

    aggregate = (math + physics + chemistry) / 3

    if (math >= 40 and physics >= 40
            and chemistry >= 40 and aggregate >= threshold):

        applicants.append({
            "id": cid,
            "name": name,
            "math": math,
            "aggregate": aggregate
        })

# Sort candidates using tie-breaking rules
applicants.sort(
    key=lambda x: (-x["aggregate"], -x["math"], x["id"])
)

# Display merit list
print("\n----- UNIVERSITY MERIT LIST -----")
print("ID\tName\tAggregate\tRank")

if len(applicants) == 0:
    print("No eligible candidates found")
else:
    for rank, student in enumerate(applicants, 1):
        print(student["id"], student["name"],
              round(student["aggregate"], 2),
              rank, sep="\t")

