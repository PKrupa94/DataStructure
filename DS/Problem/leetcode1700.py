def countStudents(students, sandwiches):
    temp = 0
    while students:
        if students[0] == sandwiches[0]:
            temp = 0
            students.pop(0)
            sandwiches.pop(0)
        else:
            temp += 1
            students.append(students.pop(0))
            if temp >= len(students):
                break
    return len(students)
