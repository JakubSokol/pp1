import json


def f(age,course,average):
    student_quantity = 0
    p=open("test.json","r")
    x=json.load(p)

    for student in x:
        found_age = student["age"]
        found_courses = student["studies"]["courses"]
        found_grades = None
        for elem in found_courses:
            if elem["name"] == course:
                found_grades = elem["grades"]
        
        if found_grades:
            if age <= found_age:
                average_grade = sum(found_grades) / len(found_grades)
                if average <= average_grade:
                    student_quantity += 1
    
    return student_quantity

print(f(21, "statistics", 4)) 