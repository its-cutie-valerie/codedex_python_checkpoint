import os

os.system('cls' if os.name == 'nt' else 'clear')
while True:
    print("Welcome to my checkpoint project!"
        "\nAvailable Shapes:"
        "\n\n1. Square - requires one dimension: side length"
        "\n2. Rectangle - requires two dimensions: length and width"
        "\n3. Triangle - requires two dimensions: base and height"
        "\n4. Circle - requires one dimension: radius"
        "\n0. Exit")

    try:
        choice = int(input("\nSelect a shape (0 to exit): "))
        
        if choice == 0:
            print("Made with ❤️ by Valérie. Thank you for everything you all have done with Codédex, super cool and fun service to use! Keep up the great work! 🚀")
            break
        
        if choice == 1:
            side = float(input("Enter the side length of the square: "))
            print("The area of the square is: ", side**2)
        elif choice == 2:
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print("The area of the rectangle is: ", length*width)
        elif choice == 3:
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            print("The area of the triangle is: ", 0.5*base*height)
        elif choice == 4:
            radius = float(input("Enter the radius of the circle: "))
            print("The area of the circle is: ", 3.14*radius**2)
        else:
            print("Invalid choice. Please select a valid option.")
            
    except ValueError:
        print("Invalid input. Please enter a number.")
