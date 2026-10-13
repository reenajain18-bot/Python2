
print("=== Power Calculator ===")

# PART 1: Ask the two questions
base = int(input("Enter the base number: "))
exponent = int(input("Enter the power: "))

# PART 2: The running total
result = 1

# PART 3 + 4: The loop that multiplies
for i in range(1, exponent + 1):
    result = result * base
    print("Step", i, "Result =", result)

# PART 5: Display the answer
print(base, "raised to the power", exponent, "is", result)
