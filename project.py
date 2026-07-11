# STUDENTS GRADES ANALYZER

print("STUDENTS GRADE ANALYZER PROJECT")

print("-------------------------------")

std_name = input("Enter your name : ")
subjects = int(input("Enter total subjects: "))

if subjects <= 0:
    print("Number of subjects must be greater than zero.... ")
    exit()


max_marks = float(input("Enter maximun marks per subjects: "))

total = subjects * max_marks
obtained_marks = 0

for i in range(subjects):
    while True:
        marks = float(input(f"Enter marks of subject {i+1}: "))
        if 0 <= marks <= max_marks:
            obtained_marks += marks
            break
        else:
            print(f"Invalid!! Enter marks between 0 and {max_marks}")


percentage = (obtained_marks / 100) * 100

if(percentage >= 90):
    grade = "A+"
elif(percentage >= 80):
    grade = "A"
elif(percentage >= 70):
    grade = "B"
elif(percentage >= 60):
    grade = "C"
else:
    grade = "F"


status = "PASS" if percentage >= 40 else "FAIL"


print()
print("-----------RESULT-----------")
print()

print(f"Student name : {std_name} ")
print(f"Total Marks : {total}")
print(f"Obtained Marks : {obtained_marks}")
print(f"Percentage : {percentage}")
print(f"Grade : {grade}")
print(f"Staus : {status}")