import random

# Define the material prices and densities globally
material_prices = {
    "steel": 12,  # SEK per kg
    "stainless_steel": 18,  # SEK per kg
    "aluminum": 50,          # SEK per kg
    "custom": 0              # SEK per kg (for custom material, price will be entered by the user)
}

material_densities = {
    "steel": 7.85,  # g/cm^3
    "stainless_steel": 7.85,  # g/cm^3
    "aluminum": 2.70,         # g/cm^3
    "custom": 0              # density for custom material will be entered by the user
}

def calculate_mass(length, width, thickness, material):
    # Get the density of the material
    density = material_densities.get(material, 0)  # Default density is 0 if material is unknown
    
    # Convert mm^3 to cm^3 (1 mm^3 = 0.001 cm^3)
    volume = (length / 10) * (width / 10) * (thickness / 10)  # volume in cm^3
    mass = volume * density  # mass in grams (g)
    
    return mass / 1000  # convert grams to kilograms

def calculate_cost(mass, material):
    # Get the price per kg of the material
    price_per_kg = material_prices.get(material, 0)  # Default price is 0 if material is unknown
    return mass * price_per_kg  # cost in SEK

def get_input(prompt, valid_choices=None):
    """Utility function for getting input and handling 'e' to exit."""
    while True:
        user_input = input(prompt).lower()
        if user_input == 'e':
            print("Exiting the program.")
            exit()
        if valid_choices and user_input not in valid_choices:
            print("Invalid option. Please enter a valid option.")
        else:
            return user_input

def main():
    print("Welcome to the Sheet Cost Calculation CLI")

    # Ask for demo mode or manual input
    demo_mode = get_input("Do you want to run the program in demo mode? (y/n, or 'e' to quit): ", ['y', 'n'])

    # Ask for the number of sheets
    while True:
        try:
            num_sheets = int(get_input("Enter the number of sheets: "))
            if num_sheets <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # Loop through the number of sheets
    for sheet_num in range(1, num_sheets + 1):
        print(f"\nSimulating input for sheet {sheet_num}...")

        if demo_mode == 'y':
            # Generate random values for demo mode
            length = random.randint(300, 1000)  # Random length between 300mm and 1000mm
            width = random.randint(100, 600)    # Random width between 100mm and 600mm
            thickness = random.randint(1, 20)   # Random thickness between 1mm and 20mm
            material = random.choice(list(material_prices.keys()))  # Randomly choose material
        else:
            # Manual input mode for length, width, thickness, and material
            length = int(get_input(f"Enter the length for sheet {sheet_num} (in mm): "))
            width = int(get_input(f"Enter the width for sheet {sheet_num} (in mm): "))
            thickness = int(get_input(f"Enter the thickness for sheet {sheet_num} (in mm): "))

            # Display material choices
            print("\nAvailable materials:")
            print("1. Steel")
            print("2. Stainless Steel")
            print("3. Aluminum")
            print("4. Custom (enter your own material)")

            material_choice = get_input(f"Enter the material number for sheet {sheet_num}: ", ['1', '2', '3', '4'])
            if material_choice == '1':
                material = "steel"
            elif material_choice == '2':
                material = "stainless_steel"
            elif material_choice == '3':
                material = "aluminum"
            elif material_choice == '4':
                material = "custom"
                custom_price = float(get_input("Enter the price per kg for the custom material (SEK): "))
                custom_density = float(get_input("Enter the density (g/cm³) for the custom material: "))
                # Update the price and density for custom material
                material_prices["custom"] = custom_price
                material_densities["custom"] = custom_density

        print(f"  Length: {length} mm, Width: {width} mm, Thickness: {thickness} mm")
        print(f"  Material: {material}")

        mass = calculate_mass(length, width, thickness, material)
        cost = calculate_cost(mass, material)

        print(f"  Mass: {mass:.2f} kg")
        print(f"  Cost: {cost:.2f} SEK")

    # Ask if the user wants to calculate another set of sheets
    another = get_input("\nDo you want to calculate another set of sheets? (y/n, or 'e' to quit): ", ['y', 'n'])
    if another == 'y':
        main()  # Re-run the main function to calculate again
    else:
        print("Exiting the program.")

# Run the main function
if __name__ == "__main__":
    main()
