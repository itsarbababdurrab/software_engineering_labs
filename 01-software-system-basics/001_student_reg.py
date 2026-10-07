students = []


def register_student(name, email):
    student = {
        "id": len(students) + 1,
        "name": name,
        "email": email
    }

    students.append(student)

    return student


student = register_student(
    "Ali",
    "ali@example.com"
)


print(student)

print(students)