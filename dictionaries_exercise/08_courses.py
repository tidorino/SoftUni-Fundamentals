def courses():

    courses_dict = {}
    numb_student = 0
    while True:
        command = input()

        if command == 'end':
            break
        info = command.split(" : ")
        course = info[0]
        student_name = info[1]
        if course not in courses_dict:
            courses_dict[course] = {}
            courses_dict[course] = [student_name]

        else:
            courses_dict[course] += [student_name]
    for key, value in courses_dict.items():
        value1 = len(value)

        print(f'{key}: {value1}')
        for i in range(len(value)):
            print(f'-- {value[i]}')


courses()
