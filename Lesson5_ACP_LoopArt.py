
# ================================
# LOOP ART DESIGNER
# ================================

# PART 1: Star Pyramid Pattern
print("===== STAR PYRAMID PATTERN =====")

rows = int(input("Enter number of rows for star pattern: "))

for i in range(rows):
    for j in range(i + 1):
        print("* ", end="")
    print()


# PART 2: Floyd's Triangle Pattern
print("\n===== FLOYD'S TRIANGLE =====")

rows = int(input("Enter number of rows for Floyd's Triangle: "))
number = 1

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(number, end=" ")
        number += 1
    print()


# PART 3: Diamond Number Pattern
print("\n===== DIAMOND NUMBER PATTERN =====")

row_size = int(input("Enter number of rows for diamond pattern: "))

if row_size % 2 == 0:
    half_rows = row_size // 2
else:
    half_rows = row_size // 2 + 1

space = half_rows - 1

# Upper half of diamond
for i in range(1, half_rows + 1):

    for j in range(1, space + 1):
        print(" ", end="")

    space -= 1
    number = 1

    for j in range(2 * i - 1):
        print(number, end="")
        number += 1

    print()

# Lower half of diamond
space = 1

for i in range(1, half_rows):

    for j in range(1, space + 1):
        print(" ", end="")

    space += 1
    number = 1

    for j in range(1, 2 * (half_rows - i)):
        print(number, end="")
        number += 1

    print()


# PART 4: Final Message
print("\n===== LOOP ART DESIGN COMPLETE =====")
print("You created star, triangle, and diamond patterns using nested loops!")
