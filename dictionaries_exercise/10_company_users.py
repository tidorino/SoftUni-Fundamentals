def company_info():

    company_dict = {}

    while True:
        command = input()

        if command == 'End':
            break
        info = command.split(" -> ")
        company_name = info[0]
        employee_id = info[1]
        if company_name not in company_dict:
            company_dict[company_name] = {}
            company_dict[company_name] = [employee_id]

        else:
            if employee_id not in company_dict[company_name]:
                company_dict[company_name] += [employee_id]

    for key, value in company_dict.items():
        print(f'{key}')
        for i in range(len(value)):
            print(f'-- {value[i]}')


company_info()
