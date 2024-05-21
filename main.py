while True:
    y = (input("Enter the word: "))
    if y != y :
        print('y')

    elif y == '#':
        print("Invalid input")
        break

    n1 = float(input("Enter the first number: "))
    operator = (input("Enter the operator: "))
    n2 = float(input("Enter the second number: "))

    if operator == "+":
        n3 = n1 + n2
        print(n3)
        continue
    elif operator == "-":
        n3 = n1 - n2
        print(n3)
        continue
    elif operator == "*":
        n3 = n1 * n2
        print(n3)
        continue
    elif operator == "/":
        n3 = n1 / n2
        print(n3)
        continue
    else:
        print("Invalid operator")
         
