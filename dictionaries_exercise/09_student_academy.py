def student_academy():
    number = int(input())
    student_info = {}
    for n in range(number):
        name = input()
        grade = float(input())
        if name not in student_info:

            student_info[name] = [grade]
        else:
            student_info[name] += [grade]

    for key, value in student_info.items():
        average_grade = sum(value) / len(value)
        if average_grade >= 4.50:
            print(f'{key} -> {average_grade:.2f}')


student_academy()
