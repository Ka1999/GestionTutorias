students = []
subjects = []
sesions = []
tutors = []

def add_student():
    id_student = int(input("Ingresa tu id: "))
    name_student = input ("Ingresa tu nombre: ")
    career_student = input ("Ingresa tu carrera: ")
    
    student = {
        "id" : id_student,
        "name" : name_student,
        "career" : career_student
     }
    global students
    students.append(student)
    print(students)

def add_subject():
    pass

def add_session():
    pass

def add_tutor():
    pass

add_student()
add_student()
add_student()
