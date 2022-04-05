def factorial_num(n1, n2):
    value_numb1 = 1
    value_numb2 = 1
    for i in range(1, n1 + 1):
        value_numb1 *= i
    for y in range(1, num2 + 1):
        value_numb2 *= y
    result = value_numb1 / value_numb2
    print(f'{result:.2f}')


num1, num2 = int(input()), int(input())
factorial_num(num1, num2)