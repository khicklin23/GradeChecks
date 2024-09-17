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
        next(csv_reader)
        
        for row in csv_reader:
            #Only 1 comma/line in .csv so we format it ourselves 
            SID = row[0].split(' ')
            firstN = SID[1]
            contents = (row[1])  
            member_info = contents.split(' ')
            #Format Name
            name = member_info[1] + " " + firstN
            #Grab GPA
            gpa = member_info[6]
            #Pass GPA to Study Hours Calculator
            hours = calculate_required_hours(float(gpa))
            print(f"{name} , GPA: {gpa} , Study Hours: {hours}" )
            
file_path = 'grades.csv'
process_grades(file_path)