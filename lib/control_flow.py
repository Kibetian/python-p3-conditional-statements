#!/usr/bin/env python3


def admin_login(username, password):
    # your code here
    if (username == 'admin' or username == 'ADMIN') and password =='12345':
        return 'Access granted'
    else:
        return 'Access denied'
# username = input('Enter username: ')            
# password=input('Enter password: ')

# Access = admin_login(username, password)
# print(Access)

def hows_the_weather(temperature):
    # your code here
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!" 
    elif temperature >85:
        return "It's too dang hot out there!" 
    else:
        return "It's perfect out there!"             
# temperature = float(input('Enter the tempereture: '))
# weather_feedback = hows_the_weather(temperature)
# print(weather_feedback)        

def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz" 
    else:
        return num            
# print(fizzbuzz(1))

def calculator(operation, num1, num2):
    # your code here
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2    
    elif operation == '*':
        return num1 * num2 
    elif operation == '/':
        if num2 != 0:
            return num1 / num2 
        else:
            return "Cannot divide by zero!"
    else:
        return "Invalid operation!"             
# print(calculator('+', 10, 6))  
    


    