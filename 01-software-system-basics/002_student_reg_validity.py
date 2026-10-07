students = []


def register_student(name, email):

    if not name.strip():
        return {
            "success": False,
            "message": "Name is required"
        }

    if "@" not in email:
        return {
            "success": False,
            "message": "Invalid email"
        }

    student = {
        "id": len(students) + 1,
        "name": name,
        "email": email
    }

    students.append(student)

    return {
        "success": True,
        "student": student
    }



student = register_student("Ali", "ali@example.com")

student = register_student("Ali", "ali@example.com")

student = register_student("Ali Again", "ali@example.com")


print(student)

print(students)