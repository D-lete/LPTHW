def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b


def subtract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b


def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b


def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some match with just functions:")

age = add(25, 5)
height = subtract(72, 0)
weight = multiply(40, 4)
iq = divide(390, 3)

print(f"Age: {age}\n Height: {height}\n Weight: {weight}\n IQ: {iq}\n")

# A puzzle for extra credit:

print("Here is a puzzle: ")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print(f"What is equal to {what}.")
