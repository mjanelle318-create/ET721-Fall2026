"""
JAnelle Moncrieffe
lab 6
Sep 23, 2026
"""
print("\n example [1])")

with open("phrases.txt", "r") as file1:
    FileContent = file1.read()
    print(FileContent)
    print(f"Is the file closed? {file1.closed}")

with open("phrases.txt", "r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))

print("\n example [2])")

with open("phrases.txt", "r") as file1:
    print(file1.read(30))
    print(file1.read(5))

print("\n example [3])")

with open("phrases.txt", "r") as file1:
    print(file1.readline(30))
    print(file1.readline(5))

print("\n example [4])")

with open("phrases.txt", "r") as file1:
    print(file1.readlines())

print("\n example [5])")

with open("phrases.txt", "r") as file1:
    filelines = file1.readlines()
    for eachline in filelines:
        print(eachline.strip())

print("\n example [6])")

with open("lastname.txt", "w") as file:
    file.write("Python Basics for Data Science\n")
    file.write("Type your full name in this line")

print("\n example [7])")

from datetime import datetime

with open("lastname.txt", "a") as file:
    file.write(f"\n{datetime.now()}")


print("\n Exercise 1")

with open("notes.txt", "r") as file:
    content = file.read()

print(content)
print("Number of characters:", len(content))
print("Number of lines:", len(content.splitlines()))


print("\n Exercise 2")

with open("tasks.txt", "w") as file:
    for i in range(1, 4):
        task = input(f"Enter task {i}: ")
        file.write(task + "\n")

print("Tasks saved to tasks.txt")


print("\n Exercise 3")

task = input("Enter a new task: ")

with open("tasks.txt", "a") as file:
    file.write(task + "\n")

print("Task added successfully.")


print("\n Exercise 4")

total_sales = 0
count = 0

with open("sales.txt", "r") as file:
    for line in file:
        name, sales = line.strip().split(",")
        sales = int(sales)

        print(f"{name}: ${sales}")

        total_sales += sales
        count += 1

average_sales = total_sales / count

print(f"\nTotal sales: ${total_sales}")
print(f"Average sales: ${average_sales:.2f}")


print("\n Exercise 5")

while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Calculate total")
    print("4. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        category = input("Enter category: ")
        amount = input("Enter amount: ")

        with open("expenses.txt", "a") as file:
            file.write(f"{category},{amount}\n")

        print("Expense added.")

    elif choice == "2":
        with open("expenses.txt", "r") as file:
            print("\nExpenses:")

            for line in file:
                category, amount = line.strip().split(",")
                print(f"{category}: ${float(amount):.2f}")

    elif choice == "3":
        total = 0

        with open("expenses.txt", "r") as file:
            for line in file:
                category, amount = line.strip().split(",")
                total += float(amount)

        print(f"Total expenses: ${total:.2f}")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")


print("\n Exercise 6")

import pandas as pd

df = pd.read_csv("sales.txt", names=["Name", "Sales"])

print("\nDataFrame:")
print(df)

print("\nFirst 3 rows:")
print(df.head(3))

print("\nLast 2 rows:")
print(df.tail(2))

print("\nTotal sales:")
print(df["Sales"].sum())

print("\nAverage sales:")
print(df["Sales"].mean())

print("\nEmployee with highest sales:")
print(df.loc[df["Sales"].idxmax()])

print("\nEmployee with lowest sales:")
print(df.loc[df["Sales"].idxmin()])

print("\nEmployees with sales greater than $100:")
print(df[df["Sales"] > 100])