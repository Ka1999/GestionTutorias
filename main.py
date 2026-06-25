students = []
subjects = []
sessions = []
tutors = []

def add_student():
    id_student = int(input("Ingresa tu id: "))
    name_student = input("Ingresa tu nombre: ")
    career_student = input("Ingresa tu carrera: ")
    
    student = {
        "id" : id_student,
        "name" : name_student,
        "career" : career_student
     }
    global students
    students.append(student)
    print(students)

def add_subject():
    id_subject = int(input("Ingresa el id de la materia: "))
    name_subject = input("Ingresa el nombre de la materia: ")

    subject = {
        "id" : id_subject,
        "name" : name_subject
        }
    global subjects
    subjects.append(subject)
    print(subjects)

def add_session():
    id_student = int(input("Ingresa tu id: "))
    id_tutor =  input("Ingresa el nombre de la materia: ")
    id_subject = int(input("Ingresa el id de la materia: "))
    hour_sesion = int(input("Ingresa tu id: "))

    session = {
        "id_student" : id_student,
        "id_tutor" : id_tutor,
        "id_subject" : id_subject,
        "hour_sesion" : hour_sesion
    }
    global sessions
    sessions.append(session)
    print(sessions)

def add_tutor():
    id_tutor = input("Ingresa el nombre de la materia: ")
    name_tutor = input("Ingresa tu nombre: ")

    tutor = {
        "id_tutor" : id_tutor,
        "name_tutor" : name_tutor
    }
    global tutors
    tutors.append(tutor)
    print(tutors)

add_student()
add_student()
add_student()
