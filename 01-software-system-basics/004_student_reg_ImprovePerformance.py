students_by_email = {}


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

    if email in students_by_email:
        return {
            "success": False,
            "message": "Email already exists"
        }

    student = {
        "id": len(students_by_email) + 1,
        "name": name,
        "email": email
    }

    students_by_email[email] = student

    return {
        "success": True,
        "student": student
    }


student = register_student("Ali", "ali@example.com")

student = register_student("Ali", "ali@example.com")

student = register_student("Ali Again", "ali@example.com")

student = register_student("Ali 2 Again", "ali2@example.com")

student = register_student("Ali 3 Again", "ali3@example.com")


# print(student)

print(students_by_email)