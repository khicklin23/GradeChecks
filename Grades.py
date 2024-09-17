import csv

def calculate_required_hours(gpa):
    if gpa < 2.5:
        return 8
    elif 2.5 <= gpa < 3.0:
        return 5
    elif 3.0 <= gpa < 3.5:
        return 3
    else:
        return 0

def process_grades(file_path):
    with open(file_path, mode='r') as file:
        csv_reader = csv.reader(file)
        
        # Skipping the header row if it exists
        next(csv_reader)
        
        for row in csv_reader:
            name = row[1]
            gpa = float(row[6])  
            
            required_hours = calculate_required_hours(gpa)
            
            print(f"Name: {name}, Required Study Hours: {required_hours}")

file_path = 'grades.csv'
process_grades(file_path)
