def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    if y == 0:
        return "Cannot divide by zero"
    return x/y

if __name__ == "__main__":
    print("Choose Operation to be performed:")
    op = input("Enter your choice:")
    num1 = int(input(print("Enter first number")))
    num2 = int(input(print("Enter Second Number")))

    if op == '1':
        print(f"Result: {add(num1, num2)}")
    elif op == '2':
        print(f"Result: {subtract(num1, num2)}")
    elif op == '3':
        print(f"Result: {multiply(num1, num2)}")
    elif op == '4':
        print(f"Result: {divide(num1, num2)}")
    else:
        print("Invalid Choice!")
