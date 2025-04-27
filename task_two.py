def base_operations(numbers: list, operations: list) -> None:
    operation = operations.pop()
    b = numbers.pop()
    a = numbers.pop() if numbers else 0
    if operation == "+":
        numbers.append(int(a) + int(b))
    elif operation == "-":
        numbers.append(int(a) - int(b))
    else:
        raise "Недопустимый оператор"


def calculate(string):
    operations = []
    numbers = []
    counter = 0
    len_string = len(string)
    while counter < len_string:
        char = string[counter]
        if char == ' ':
            counter += 1
            continue
        elif char == '(':
            operations.append(char)
            counter += 1
        elif char == ')':
            while operations and operations[-1] != '(':
                base_operations(numbers, operations)
            operations.pop()
            counter += 1
        elif char in '+-':
            if char == '-' and (counter == 0 or string[counter - 1] == '('):
                numbers.append(0)
            while operations and operations[-1] != '(':
                base_operations(numbers, operations)
            operations.append(char)
            counter += 1
        else:
            num = 0
            while counter < len_string and string[counter].isdigit():
                num = num * 10 + int(string[counter])
                counter += 1
            numbers.append(num)

    while operations:
        base_operations(numbers, operations)

    return numbers[-1]

print(calculate('-((5 - 2) - (3) + 2) + 1'))
