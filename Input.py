calculation_to_units=24
name_of_unit="hours"


def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def calc():
    try:
        user_input_int = int(num_of_run)
        if user_input_int > 0:
            calculated_value = days_to_units(user_input_int)
            print(calculated_value)
        elif user_input_int == 0:
            print("Enter a valid number greater than 0")
        else:
            print("Enter a valid number greater than 0")
    except ValueError:
        print("Enter only valid and non-floating digits, texts not acceptable")


user_input = ""
while user_input != "exit":
    user_input = input("Please enter number of days and i will convert it to hours\n")
    for num_of_run in user_input.split(","):
        calc()
