import random
import time

# Function to generate random sheet data for demo mode
def generate_random_sheet_data():
    # Reasonable ranges for the sheet dimensions (in mm)
    length = random.randint(200, 1000)  # Length between 200 mm and 1000 mm
    width = random.randint(200, 1000)   # Width between 200 mm and 1000 mm
    thickness = random.choice([2, 3, 4, 5, 6, 8, 10])  # Random thickness from a list of options
    return {"length": length, "width": width, "thickness": thickness}

# Function to generate a random density for demo mode
def generate_random_density():
    densities = [7.85, 7.95, 2.70]
    return random.choice(densities)

# Function to get sheet data (with demo mode option)
def get_sheet_data(demo_mode=False):
    sheets = []
    num_sheets = input("Enter the number of sheets (or type 'exit' to quit): ").strip().lower()
    if num_sheets == 'exit':
        return 'exit'
    
    # Handle demo mode
    num_sheets = int(num_sheets) if not demo_mode else random.randint(1, 5)  # Random number of sheets (1-5)

    for i in range(num_sheets):
        if demo_mode:
            print(f"\nSimulating input for sheet {i + 1}...")
            time.sleep(1)  # Simulate delay between inputs
            sheet = generate_random_sheet_data()
            print(f"Length: {sheet['length']} mm, Width: {sheet['width']} mm, Thickness: {sheet['thickness']} mm")
        else:
            print(f"\nEnter details for sheet {i + 1}:")
            length = input("Enter length (in mm, or type 'exit' to quit): ").strip()
            if length.lower() == 'exit':
                return 'exit'
            if not length.isdigit():
                print("Invalid input. Please enter a valid number for length.")
                continue
            length = int(length)
            
            width = input("Enter width (in mm, or type 'exit' to quit): ").strip()
            if width.lower() == 'exit':
                return 'exit'
            if not width.isdigit():
                print("Invalid input. Please enter a valid number for width.")
                continue
            width = int(width)

            thickness = input("Enter thickness (in mm, or type 'exit' to quit): ").strip()
            if thickness.lower() == 'exit':
                return 'exit'
            if not thickness.isdigit():
                print("Invalid input. Please enter a valid number for thickness.")
                continue
            thickness = int(thickness)

            sheet = {"length": length, "width": width, "thickness": thickness}
        
        sheets.append(sheet)
        if demo_mode:
            time.sleep(1)  # Simulate slight delay between entries

    return sheets

# Function to select the density with notes
def select_density(demo_mode=False):
    if demo_mode:
        # In demo mode, randomly generate a density
        density = generate_random_density()
        print(f"\nSimulating density selection... Selected density: {density} kg/dm^3")
        return density
    else:
        print("\nSelect density from the following options:")
        print("1. 7.85 kg/dm^3 (Stål - Steel)")
        print("2. 7.95 kg/dm^3 (Rostfritt - Stainless Steel)")
        print("3. 2.70 kg/dm^3 (Aluminium)")
        print("4. Custom density")

        while True:
            option = input("Enter your choice (1-4, or 'exit' to quit): ").strip().lower()
            if option == 'exit':
                return 'exit'
            
            if option in ['1', '2', '3']:
                option = int(option)
                break
            elif option == '4':
                custom_density = input("Enter custom density (in kg/dm^3, or 'exit' to quit): ").strip()
                if custom_density.lower() == 'exit':
                    return 'exit'
                try:
                    custom_density = float(custom_density)
                    return custom_density
                except ValueError:
                    print("Invalid input. Please enter a valid numeric density value.")
                    continue
            else:
                print("Invalid choice. Please select a valid option.")

        if option == 1:
            return 7.85
        elif option == 2:
            return 7.95
        elif option == 3:
            return 2.70

# Function to calculate the volume, mass, and cost
def calculate_cost(density, price_per_kg, sheets):
    results = []
    for sheet in sheets:
        volume_mm3 = sheet["length"] * sheet["width"] * sheet["thickness"]
        volume_dm3 = volume_mm3 / 1000000.0  # Convert mm^3 to dm^3
        mass_kg = volume_dm3 * density
        cost_sek = mass_kg * price_per_kg
        results.append({"mass_kg": mass_kg, "cost_sek": cost_sek})
    return results

# Main function to control the flow
def main():
    while True:
        demo_mode = input("Do you want to run the program in demo mode? (y/n, or 'e' to quit): ").strip().lower()
        if demo_mode == 'e':
            print("Exiting the program. Goodbye!")
            break  # Exit the loop and end the program
        elif demo_mode not in ['y', 'n']:
            print("Invalid option. Please type 'y' (yes), 'n' (no), or 'e' (exit).")
            continue

        # Get number of sheets from the user or demo mode (this should be asked only once)
        sheets_count = input("Enter the number of sheets (or type 'exit' to quit): ").strip().lower()
        if sheets_count == 'exit':
            print("Exiting the program. Goodbye!")
            break  # Exit the program if 'exit' was typed
        try:
            sheets_count = int(sheets_count)
        except ValueError:
            print("Invalid input. Please enter a valid number for sheets count.")
            continue

        # Get sheet data from the user or demo mode (don't prompt again)
        sheets = get_sheet_data(sheets_count, demo_mode == 'y')  # Pass sheets_count as an argument

        if sheets == 'exit':
            print("Exiting the program. Goodbye!")
            break  # Exit the program if 'exit' was typed

        # Select the density
        density = select_density(demo_mode == 'y')
        if density == 'exit':
            print("Exiting the program. Goodbye!")
            break  # Exit the program if 'exit' was typed

        # Define the price per kg
        price_per_kg = 12.5  # SEK per kg

        # Perform the calculations
        results = calculate_cost(density, price_per_kg, sheets)

        # Display the results
        print("\nCalculated Results:")
        for i, result in enumerate(results):
            print(f"\nSheet {i + 1}:")
            print("  Mass: %.2f kg" % result["mass_kg"])
            print("  Cost: %.2f SEK" % result["cost_sek"])

        # Ask the user if they want to calculate another sheet
        repeat = input("\nDo you want to calculate another sheet? (y/n, or 'e' to quit): ").strip().lower()
        if repeat == 'e':
            print("Exiting the program. Goodbye!")
            break  # Exit the program if 'e' was typed
        elif repeat == 'n':
            print("Exiting the program. Goodbye!")
            break  # Exit the program if 'n' was typed
        elif repeat != 'y':
            print("Invalid option. Please type 'y' (yes), 'n' (no), or 'e' (exit).")
            continue


# Function to get sheet data (with demo mode option)
def get_sheet_data(num_sheets, demo_mode=False):
    sheets = []
    for i in range(num_sheets):
        if demo_mode:
            print(f"\nSimulating input for sheet {i + 1}...")
            time.sleep(1)  # Simulate delay between inputs
            sheet = generate_random_sheet_data()
            print(f"Length: {sheet['length']} mm, Width: {sheet['width']} mm, Thickness: {sheet['thickness']} mm")
        else:
            print(f"\nEnter details for sheet {i + 1}:")
            length = input("Enter length (in mm, or type 'exit' to quit): ")
            if length.lower() == 'exit':
                return 'exit'
            length = int(length)
            width = input("Enter width (in mm, or type 'exit' to quit): ")
            if width.lower() == 'exit':
                return 'exit'
            width = int(width)
            thickness = input("Enter thickness (in mm, or type 'exit' to quit): ")
            if thickness.lower() == 'exit':
                return 'exit'
            thickness = int(thickness)
            sheet = {"length": length, "width": width, "thickness": thickness}
        
        sheets.append(sheet)
        if demo_mode:
            time.sleep(1)  # Simulate slight delay between entries

    return sheets

# Run the program
if __name__ == "__main__":
    main()
