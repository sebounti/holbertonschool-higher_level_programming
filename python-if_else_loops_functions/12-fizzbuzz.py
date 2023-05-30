#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("fizzbuz", end="")
        elif number % 3 == 0:
            print("fizz", end=" ")
        elif number % 5 == 0:
            print("buzz", end=" ")
        else:
            print(number, end=" ")
