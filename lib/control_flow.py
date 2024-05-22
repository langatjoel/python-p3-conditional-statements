# lib/control_flow.py

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    return "Access denied"

def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature < 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

def fizzbuzz(n):
    if n % 15 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

# lib/control_flow.py

def calculator(a, operator, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print("Invalid input! Please provide numerical values.")
        return None
    
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        if b == 0:
            print("Cannot divide by zero!")
            return None
        return a / b
    else:
        print("Invalid operation!")
        return None
