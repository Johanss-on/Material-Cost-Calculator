# Sheet Cost Calculation CLI

## Overview
This Python script calculates the mass and cost of metal sheets based on user input or generates simulated data for demonstration purposes. It allows users to input sheet dimensions, select material density, and calculate the total cost based on weight.

## Requirements
- Python 3.7+ (You can download it from [here](https://www.python.org/downloads/))
- The script uses the built-in `random` and `time` libraries.

## How to Use

1. Clone or download the `calculate_sheet_cost_CLI.py` script.
2. Open a terminal (or command prompt) and navigate to the directory where the script is located.
3. Run the script by typing the following command:
    ```bash
    python calculate_sheet_cost_CLI.py
4. The program will prompt you for the following inputs:
- **Demo Mode**: Choose whether to run in demo mode (simulating random data) or manual input mode.
- **Number of Sheets**: Enter the number of sheets you want to calculate.
- **Material**: Choose a material from the list by entering the corresponding number:
  - 1: Steel
  - 2: Stainless Steel
  - 3: Aluminum
  - 4: Custom (Enter your custom density in kg/dm³)
- **Sheet Dimensions**: Enter the length, width, and thickness of the sheets (in millimeters).
- **Density**: For the selected material, the script will either use a predefined density or ask for a custom density input.

5. For each sheet, the program will calculate and display:
- Length, Width, Thickness
- Material and Density used
- Mass and Cost

6. If you want to exit the program at any time, type `e`.

## Example Usage

```text
Do you want to run the program in demo mode? (y/n, or 'e' to quit): y
Enter the number of sheets: 3

Simulating input for sheet 1...
Length: 479 mm, Width: 429 mm, Thickness: 10 mm
Material: Steel
Mass: 16.44 kg
Cost: 1643.93 SEK

Simulating input for sheet 2...
Length: 832 mm, Width: 520 mm, Thickness: 12 mm
Material: Stainless Steel
Mass: 20.00 kg
Cost: 2000.00 SEK

Simulating input for sheet 3...
Length: 900 mm, Width: 500 mm, Thickness: 8 mm
Material: Aluminum
Mass: 15.00 kg
Cost: 1500.00 SEK

Do you want to calculate another sheet? (y/n, or 'e' to quit):
``````

# Technical Details

The script uses basic mathematical calculations to determine the volume and mass of a sheet based on the input dimensions. The mass is then multiplied by the selected material density to calculate the final weight. The price is calculated based on the mass, with a fixed price per kilogram for each material.

# Contact

For any issues or questions, feel free to reach out to the developer: Lucas Johansson.
