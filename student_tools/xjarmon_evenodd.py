TOOL_NAME = "Even or Odd"

def run():
    print("This is a Python program that checks if a number is Even or Odd.")
    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

run()
