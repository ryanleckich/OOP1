import studentclass as sc

studentID = input("Student ID: ")
DOB = input("Date of Birth: ")
DOB = int(DOB.split("/")[2])

name = input("Name: ")
classification = input(" classification - 'Sr','Jr','S' or 'F'): ")

my_student = sc.Student(studentID, name, DOB, classification)
