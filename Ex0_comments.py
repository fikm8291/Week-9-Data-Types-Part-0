# -------------------------------------------
# Exercise 0: Comments Practice
# -------------------------------------------
# In this exercise, you'll practice writing clear, helpful comments
# to explain Python code.
#
# Good comments should:
# - Explain WHAT the code does (not just repeat it)
# - Be clear and concise
# - Help someone else understand your code
#
# Below you'll find several code snippets.
# Add comments to explain what each section does.
# -------------------------------------------

# -------------------------------------------
# Task 1: Shopping Cart
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 1: Shopping Cart\n"
      + "-------------------------------------------")

# Add comments to explain this code:

cart = ["apple", "bread", "milk", "eggs"]
total_items = len(cart)

print(f"You have {total_items} items in your cart")

for item in cart:
    print(f"- {item}")

# -------------------------------------------
# Task 2: Grade Calculator
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 2: Grade Calculator\n"
      + "-------------------------------------------")

# Add comments to explain this code:

score = int(input("Enter your test score: "))

if score >= 70:
    grade = "Pass"
else:
    grade = "Fail"

print(f"Your grade: {grade}")

# -------------------------------------------
# Task 3: Password Validator
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 3: Password Validator\n"
      + "-------------------------------------------")

# Add comments to explain this code:

password = input("Create a password: ")

is_long = len(password) >= 8
has_upper = password != password.lower()
has_lower = password != password.upper()

is_valid = is_long and has_upper and has_lower

if is_valid:
    print("Password accepted!")
else:
    print("Password rejected. Must be 8+ characters with upper and lowercase letters.")

# -------------------------------------------
# Task 4: Even Number Counter
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 4: Even Number Counter\n"
      + "-------------------------------------------")

# Add comments to explain this code:

numbers = [12, 7, 18, 5, 22, 9, 14]
even_count = 0

for num in numbers:
    if num % 2 == 0:
        even_count = even_count + 1

print(f"There are {even_count} even numbers in the list")

# -------------------------------------------
# Task 5: Student Records
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 5: Student Records\n"
      + "-------------------------------------------")

# Add comments to explain this code:

student = {
    "name": "Alice",
    "age": 20,
    "grades": [85, 92, 78, 88]
}

average = sum(student["grades"]) / len(student["grades"])
average = round(average, 2)

print(f"Student: {student['name']}")
print(f"Age: {student['age']}")
print(f"Average grade: {average}")

# -------------------------------------------
# Task 6: Countdown Timer
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 6: Countdown Timer\n"
      + "-------------------------------------------")

# Add comments to explain this code:

countdown = 5

while countdown > 0:
    print(countdown)
    countdown = countdown - 1

print("Blast off!")

# -------------------------------------------
# Task 7: Menu Formatter
# -------------------------------------------
print("-------------------------------------------\n"
      + "Task 7: Menu Formatter\n"
      + "-------------------------------------------")

# Add comments to explain this code:

menu_items = ["burger", "pizza", "salad", "pasta"]
counter = 1

for item in menu_items:
    formatted_item = item.upper()
    print(f"{counter}. {formatted_item}")
    counter = counter + 1

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you've added comments to all tasks:
# 1. Save your file
# 2. Open the terminal
# 3. Use Git to:
#    - Stage your changes
#    - Commit your changes
#    - Push your changes to the external repository
# Optional: Check GitHub to confirm your changes appear.
# -------------------------------------------
