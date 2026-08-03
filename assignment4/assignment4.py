import pandas as pd
import numpy as np

# Task 1: Create a DataFrame from a dictionary

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
}

task1_data_frame = pd.DataFrame(data)

print("Original DataFrame:")
print(task1_data_frame)


# Add a Salary column to a copy

task1_with_salary = task1_data_frame.copy()

task1_with_salary["Salary"] = [70000, 80000, 90000]

print("\nDataFrame with Salary:")
print(task1_with_salary)


# Increment the Age column 

task1_older = task1_with_salary.copy()

task1_older["Age"] = task1_older["Age"] + 1

print("\nDataFrame with Ages Increased:")
print(task1_older)


# final DataFrame to a CSV file

task1_older.to_csv("employees.csv", index=False)

#Task 2: Loading Data from CSV and JSON

# Read the CSV file
task2_employees = pd.read_csv("employees.csv")

print("\nEmployees from CSV:")
print(task2_employees)

# Read the JSON file
json_employees = pd.read_json("additional_employees.json")

print("\nEmployees from JSON:")
print(json_employees)

# Combine both DataFrames
more_employees = pd.concat(
    [task2_employees, json_employees],
    ignore_index=True
)

print("\nCombined Employees:")
print(more_employees)

#Task 3: Data Inspection - Using Head, Tail, and Info Methods

# First three rows
first_three = more_employees.head(3)

print("\nFirst Three Rows:")
print(first_three)

# Last two rows
last_two = more_employees.tail(2)

print("\nLast Two Rows:")
print(last_two)

# Shape of the DataFrame
employee_shape = more_employees.shape

print("\nShape:")
print(employee_shape)

# Summary information
print("\nDataFrame Info:")
more_employees.info()

# Task 4: Data Cleaning

# Read dirty data
dirty_data = pd.read_csv("dirty_data.csv")

print("\nDirty Data:")
print(dirty_data)

# Copy
clean_data = dirty_data.copy()

# Remove duplicate rows
clean_data = clean_data.drop_duplicates()

print("\nAfter Removing Duplicates:")
print(clean_data)

# Convert Age to numeric
clean_data["Age"] = pd.to_numeric(
    clean_data["Age"],
    errors="coerce"
)

print("\nAfter Converting Age:")
print(clean_data)

# Clean Salary
clean_data["Salary"] = clean_data["Salary"].replace(
    ["unknown", "n/a"],
    np.nan
)

clean_data["Salary"] = pd.to_numeric(
    clean_data["Salary"],
    errors="coerce"
)

print("\nAfter Converting Salary:")
print(clean_data)

# Fill missing values
clean_data["Age"] = clean_data["Age"].fillna(
    clean_data["Age"].mean()
)

clean_data["Salary"] = clean_data["Salary"].fillna(
    clean_data["Salary"].median()
)

print("\nAfter Filling Missing Values:")
print(clean_data)

# Convert Hire Date
clean_data["Hire Date"] = pd.to_datetime(
    clean_data["Hire Date"],
    format='mixed',
    errors="coerce"
)

print("\nAfter Converting Dates:")
print(clean_data)

# Clean text columns
clean_data["Name"] = (
    clean_data["Name"]
    .str.strip()
    .str.upper()
)

clean_data["Department"] = (
    clean_data["Department"]
    .str.strip()
    .str.upper()
)

print("\nFinal Clean Data:")
print(clean_data)