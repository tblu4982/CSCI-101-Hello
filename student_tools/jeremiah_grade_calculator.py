TOOL_NAME = "Jeremiah Grade Calculator"
def run():
    print(f"Welcome to the {TOOL_NAME}!")
    score = float(input("Enter your score (0-100): "))
    if score >= 90:
        print("You received an A.")
    elif score >= 80:
        print("You received a B.")
    elif score >= 70:
        print("You received a C.")
    elif score >= 60:
        print("You received a D.")
    else:
        print("You received an F.")

run()
