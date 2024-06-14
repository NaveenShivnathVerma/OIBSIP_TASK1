# BMI Calculator in Python

# Define BMI categories
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


# User input validation
def get_valid_input(prompt, min_value, max_value):
    while True:
        try:
            value = float(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Main function
def main():
    print("Welcome to the BMI Calculator!")

    # Get user's weight and height with validation
    weight = get_valid_input("Enter your weight in kilograms: ", 20, 200)
    height = get_valid_input("Enter your height in meters: ", 0.5, 2.5)

    # Calculate BMI
    bmi = weight / (height ** 2)

    # Get BMI category
    category = bmi_category(bmi)

    # Display result
    print(f"Your BMI is {bmi:.2f}, which is considered {category}.")


# Run the program
if __name__ == "__main__":
    main()
