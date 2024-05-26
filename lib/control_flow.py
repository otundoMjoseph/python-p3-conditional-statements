#!/usr/bin/env python3

def admin_login(username, password):
    if username == "admin"  and password == "12345":
        return "Access granted"
    elif username == "ADMIN":
        return "Access granted"
    elif username != "admin" or username !="ADMIN" and password != "12345":
        return "Access denied"


    

    

def hows_the_weather(temperature):
    if temperature > 85:
        return "It's too dang hot out there!"
    elif 65 <= temperature <= 85:
        return "It's perfect out there!"
    elif 55 <= temperature < 65:
        return "It's a little chilly out there!"
    elif temperature < 55:
        return "It's brisk out there!"
    else:
        return None


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num
    #calculator
def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
