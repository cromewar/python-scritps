if __name__ == "__main__":
    objetive = int(input('Choose a number: '))
    epsilon = 0.001
    low = 0.0
    high = max(1.0, objetive)
    result = (high + low)/2

    while abs(result**2 - objetive) >= epsilon:
        if result**2 < objetive:
            low = result
        else:
            high = result

        result = (high + low)/2
    
    print(f"the square root of {objetive} is {result}")