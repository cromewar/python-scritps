if __name__ == '__main__':
    objective = int(input('Choose a number: '))
    epsilon = 0.01
    step = epsilon**2
    result = 0.0

    while abs(result**2 - objective) >= epsilon and result <= objective:
        result += step

    if abs(result**2 - objective) >= epsilon:
        print(f'the square root of {objective} was not found')
    else:
        print(f'the square root of {objective} is {result}')    