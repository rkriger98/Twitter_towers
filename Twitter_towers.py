import math


def rectangular_tower(height, width):
    """
    Checks a rectangular tower with the given height and width.
    If the tower is a square or if the difference between the height and width is greater than 5,
    the function prints the area of the rectangle. otherwise it prints the perimeter of the rectangle.
    :param height: the height of the rectangle
    :param width: the width of the rectangle
    """
    if height == width or abs(height - width) > 5:
        area = height * width
        print(f"This is a rectangle with an area of {area}.")
    else:
        perimeter = 2 * (height + width)
        print(f"This is a rectangular with a perimeter of {perimeter:.2f}.")


def triangular_tower(height, base):
    """
    Checks a triangular tower with the given height and base.
    the function prompts the user to choose between calculating the perimeter of the triangle or printing the triangle,
    and performs the requested accordingly.
    :param height: the height of the triangle
    :param base: the base width of the triangle
    """
    print("1. Calculate the perimeter of the triangle.")
    print("2. Print the triangle.")
    choice = input("Please select an option (1-2): ")

    if choice == "1":
        side = math.sqrt((base / 2) ** 2 + height ** 2)
        perimeter = base + 2 * side
        print(f"The perimeter of the triangle is {perimeter:.2f}.")

    elif choice == "2":
        print_triangular_tower(round(height), round(base))
    else:
        print("Invalid choice.")


def print_triangular_tower(height, base):
    print("Please note: to print the triangular tower"
          "the length and width of the triangle will be rounded to the nearest round number:\n"
          f"Triangular tower height now is: {height}\n"
          f"Triangular tower base width now is: {base}")

    if base % 2 == 0 or base > 2 * height:
        print("Sorry, this triangle cannot be printed.")
    else:
        groups_in_body = math.ceil(base / 2) - 2
        if groups_in_body:  # if base > 3
            add_to_first_group = (height - 2) % groups_in_body
            lines_in_each_group = int((height - 2) / groups_in_body)
            num_asterisks = 1
            print("*".center(base))  # first line
            for i in range(groups_in_body):
                num_asterisks += 2
                if i == 0:
                    for j in range(add_to_first_group):
                        print(("*" * num_asterisks).center(base))
                for j in range(lines_in_each_group):
                    print(("*" * num_asterisks).center(base))
        else:
            for j in range(height - 1):
                print("*".center(base))
        print("*" * base)  # last line


def main():
    """
    Main function that prompts the user to select between checking a rectangular tower, checking a triangular tower,
    or exiting the program. The function validates user input for tower height and width/base and calls the appropriate
    function.
    """
    while True:
        print("Welcome to the Tower Builder program!\n"
              "1. Create a rectangular tower\n"
              "2. Create a triangular tower\n"
              "3. Exit")
        try:
            choice = int(input("Please select an option (1-3): "))
            if choice not in [1, 2, 3]:
                raise ValueError("Invalid choice. Please enter a number between 1 and 3.")

            if choice == 1:
                height = float(input("Please enter the height of the rectangular tower: "))
                while height < 2:
                    print("Error: height must be greater than or equal to 2.")
                    height = float(input("Please enter the height of the rectangular tower: "))
                width = float(input("Please enter the width of the rectangular tower: "))
                rectangular_tower(height, width)

            elif choice == 2:
                height = float(input("Please enter the height of the triangular tower: "))
                while height < 2:
                    print("Error: height must be greater than or equal to 2.")
                    height = float(input("Please enter the height of the triangular tower: "))
                base = float(input("Please enter the base width of the triangular tower: "))
                triangular_tower(height, base)

            elif choice == 3:
                print("Exiting the Tower Builder program. Goodbye!")
                break
        except ValueError:
            print("Invalid choice. Please enter an integer number between 1 and 3 only.")
            continue


if __name__ == '__main__':
    main()
