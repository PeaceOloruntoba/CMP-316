import csv

# Data to be written to the CSV file
data = [
    ["Peace Oloruntoba", "AUL/SCI/21/00726", "300", "01/15/2000", "Ekiti"],
    ["Akinyosoye Tobi", "AUL/SCI/21/00722", "300", "05/20/2001", "Ondo"],
    ["Peace Oloruntoba", "AUL/SCI/21/00726", "300", "01/15/2000", "Ekiti"],
    ["Akinyosoye Tobi", "AUL/SCI/21/00722", "300", "05/20/2001", "Ondo"],
    ["Peace Oloruntoba", "AUL/SCI/21/00726", "300", "01/15/2000", "Ekiti"],
    ["Akinyosoye Tobi", "AUL/SCI/21/00722", "300", "05/20/2001", "Ondo"],
    ["Peace Oloruntoba", "AUL/SCI/21/00726", "300", "01/15/2000", "Ekiti"],
    ["Akinyosoye Tobi", "AUL/SCI/21/00722", "300", "05/20/2001", "Ondo"],
    ["Peace Oloruntoba", "AUL/SCI/21/00726", "300", "01/15/2000", "Ekiti"],
    ["Akinyosoye Tobi", "AUL/SCI/21/00722", "300", "05/20/2001", "Ondo"]
]

# CSV file name
file_name = "student_records.csv"

# Writing data to CSV file
with open("student_records.csv", mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(["Student Name", "Matric No", "Level", "DOB", "State of Origin"])
    
    # Write the data rows
    writer.writerows(data)

print(f"Data written to student_records.csv")



add = lambda x, y: x+y
subtract = lambda x, y: x-y
multiply = lambda x, y: x*y
divide = lambda x, y: x/y

print(add(3,4))
print(subtract(8,1))
print(multiply(3,4))
print(divide(3,4))