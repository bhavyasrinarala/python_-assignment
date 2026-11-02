
basic = float(input("Enter Basic Pay: "))
hours = float(input("Enter Overtime Hours: "))
rate = float(input("Enter Overtime Rate: "))
incentive = float(input("Enter Incentives: "))

# Calculate allowances
allowance = basic * 0.20

# Calculate overtime pay
overtime = hours * rate

# Calculate gross salary
gross = basic + allowance + overtime + incentive

# Calculate progressive deduction
if gross <= 20000:
    deduction = gross * 0.05
elif gross <= 40000:
    deduction = gross * 0.10
else:
    deduction = gross * 0.15

# Calculate net salary
net = gross - deduction

# Display salary statement
print("\n----- SALARY STATEMENT -----")
print("Basic Pay      =", basic)
print("Allowances     =", allowance)
print("Overtime Pay   =", overtime)
print("Incentives     =", incentive)
print("Gross Salary   =", gross)
print("Deduction      =", deduction)
print("Net Salary     =", net)

