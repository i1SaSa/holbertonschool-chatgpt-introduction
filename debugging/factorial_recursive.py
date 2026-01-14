#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <number>")
        sys.exit(1)

    try:
        num = int(sys.argv[1])
        if num < 0:
            print("Please enter a non-negative integer.")
        else:
            print(factorial(num))
    except ValueError:
        print("Invalid input: Please enter an integer.")