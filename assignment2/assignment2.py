import csv
import traceback
import os
import custom_module
from datetime import datetime

#task 2: Read the employees.csv file and return a dictionary with fields and rows
def read_employees():
    employees_dict = {}
    rows = []

    try:
        with open("../csv/employees.csv", "r") as csv_file:
            employee_reader = csv.reader(csv_file)

            first_row = True

            for row in employee_reader:
                if first_row:
                    employees_dict["fields"] = row
                    first_row = False
                else:
                    rows.append(row)

            employees_dict["rows"] = rows

        return employees_dict

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , "
                f"Line : {trace[1]}, "
                f"Func.Name : {trace[2]}, "
                f"Message : {trace[3]}"
            )

        print(f"Exception type: {type(e).__name__}")

        message = str(e)

        if message:
            print(f"Exception message: {message}")

        print(f"Stack trace: {stack_trace}")


employees = read_employees()
print(employees)


#Task 3: Find the Column Index, given a column name, return the index of that column in the fields list

def column_index(column_name):
    return employees["fields"].index(column_name)

print(column_index("employee_id"))
print(column_index("first_name"))
print(column_index("phone"))


employee_id_column = column_index("employee_id")


#Task 4: Find the Employee First Name, given a row number, return the first name of that employee

def first_name(row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column]

print(first_name(2))
print(first_name(3))
print(first_name(4))

# Task 5: Find the Employee: a Function in a Function, given an employee_id, return the row of that employee

def employee_find(employee_id):

    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches = list(filter(employee_match, employees["rows"]))

    return matches

myEmployee = employee_find(5)
print(myEmployee)


# Task 6: Find the Employee with a Lambda, given an employee_id, return the row of that employee

def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

myEmployee2 = employee_find_2(6)
print(myEmployee2)

#Task 7: Sort the Rows by last_name Using a Lambda, 

def sort_by_last_name():
    last_name_column = column_index("last_name")

    employees["rows"].sort(
        key=lambda row: row[last_name_column]
    )

    return employees["rows"]

sort_by_last_name()
print(employees)

#Task 8: Create a dict for an Employee, 

def employee_dict(row):
    employee = {}

    for index, field in enumerate(employees["fields"]):
        if field != "employee_id":
            employee[field] = row[index]

    return employee

print(f"\nEmployee 1: {employee_dict(employees['rows'][0])}")

#Task 9: A dict of dicts, for All Employees, 

def all_employees_dict():
    all_employees = {}

    for row in employees["rows"]:
        employee_id = row[employee_id_column]
        all_employees[employee_id] = employee_dict(row)

    return all_employees

print(f"\nAll Employees: {all_employees_dict()}")

# Task 10: Use the os Module

def get_this_value():
    return os.getenv("THISVALUE")

print(f"\nTHISVALUE: {get_this_value()}")

#Task 11: Creating Your Own Module

def set_that_secret(value):
    custom_module.set_secret(value)

set_that_secret("fire-power")
print(f"\nSecret: {custom_module.secret}")


# Task 12: Read minutes1.csv and minutes2.csv

def read_csv_dict(filename):
    data = {}
    rows = []

    try:
        with open(filename, "r") as csv_file:
            csv_reader = csv.reader(csv_file)

            first_row = True

            for row in csv_reader:
                if first_row:
                    data["fields"] = row
                    first_row = False
                else:
                    rows.append(tuple(row))

            data["rows"] = rows

        return data

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = []

        for trace in trace_back:
            stack_trace.append(
                f"File : {trace[0]} , "
                f"Line : {trace[1]}, "
                f"Func.Name : {trace[2]}, "
                f"Message : {trace[3]}"
            )

        print(f"Exception type: {type(e).__name__}")

        message = str(e)

        if message:
            print(f"Exception message: {message}")

        print(f"Stack trace: {stack_trace}")

def read_minutes():
    minutes1 = read_csv_dict("../csv/minutes1.csv")
    minutes2 = read_csv_dict("../csv/minutes2.csv")

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

print(f"\nMinutes 1: {minutes1}")
print(f"\nMinutes 2: {minutes2}")

#Task 13: Create minutes_set

def create_minutes_set():
    minutes1_set = set(minutes1["rows"])
    minutes2_set = set(minutes2["rows"])

    minutes_set = minutes1_set.union(minutes2_set)

    return minutes_set

minutes_set = create_minutes_set()
print(f"\nMinutes Set: {minutes_set}")

# Task 14: Convert to datetime

def create_minutes_list():
    minutes = list(minutes_set)

    minutes = list(
        map(
            lambda x: (
                x[0],
                datetime.strptime(x[1], "%B %d, %Y")
            ),
            minutes
        )
    )

    return minutes

minutes_list = create_minutes_list()

print(f"\nMinutes List: {minutes_list}")

#Task 15: Write Out Sorted List

def write_sorted_list():
    minutes_list.sort(key=lambda row: row[1])

    converted_list = list(
        map(
            lambda row: (
                row[0],
                datetime.strftime(row[1], "%B %d, %Y")
            ),
            minutes_list
        )
    )

    with open("./minutes.csv", "w", newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted_list)

    return converted_list


sorted_minutes = write_sorted_list()
print(f"\nSorted Minutes: {sorted_minutes}")