# Sheet Cost Calculator

This is a Python-based tool that calculates the cost of metal sheets based on their dimensions and material density. The program allows users to input the length, width, and thickness of sheets, select the material type, and calculate the total mass and cost based on the material price per kilogram.

## Features
- **Material Selection**: Users can choose from various materials, each with a predefined price per kilogram.
- **Customizable Pricing**: The pricing for each material can easily be adjusted in the code.
- **Flexible Input**: Users can input multiple sheets and calculate their costs in bulk.

## Materials and Prices
The following materials are supported with their corresponding prices per kilogram:
- **Steel**: 12.5 SEK/kg
- **Stainless Steel**: 15.0 SEK/kg
- **Aluminium**: 10.0 SEK/kg

## Installation and Setup

To use the Sheet Cost Calculator, follow these steps:

1. Clone this repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/sheet-cost-calculator.git
    ```

2. Navigate to the directory where the script is located:
    ```bash
    cd sheet-cost-calculator
    ```

3. Ensure you have Python 3 installed. You can download it from [here](https://www.python.org/downloads/).

4. Run the script:
    ```bash
    python3 calculate_sheet_cost_CLI.py
    ```

## Usage

- When prompted, input the number of sheets you'd like to calculate.
- For each sheet, provide the length, width, and thickness in millimeters.
- Select the material from the available options (Steel, Stainless Steel, or Aluminium).
- The tool will calculate the mass of each sheet and display the cost based on the selected material.

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.
