# Inventory Management System

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)

## Description
The Inventory Management System is a Python program designed to manage inventory data for a shoe store. It allows users to perform various operations such as 
capturing shoe details, viewing all shoes, restocking, searching for a shoe, calculating the value per item, and identifying the product with the highest quantity. 
The system reads and writes data from/to a text file with a text-based interactive menu used for navigation. 

## Installation
1. Clone the repository:
  - git clone https://github.com/AntonioDiNics/InventoryManagement.git

2. Navigate to the project directory:
  - cd InventoryManagement

3. Install the required dependencies by running the following command:
  - pip install tabulate
    
4. Run the main Python file to start the program:
  - python inventory.py

## Usage
- **Read shoe data (rsd)**: Reads the shoe data from the "inventory.txt" file and initializes the shoe list.
- **Capture Shoe Details (csd)**: Allows you to capture data about a shoe and add it to the shoe list. The captured details are then saved to the "inventory.txt" file.
- **View All (va)**: Displays the details of all the shoes in a tabular format.
- **Re-stock (rs)**: Finds the shoe with the lowest quantity, prompts the user to restock it, and updates the quantity in the "inventory.txt" file.
- **Search Shoe (ss)**: Searches for a shoe by its code and displays its details if found.
- **Value Per Item (vpi)**: Calculates the total value for each item (shoe) and prints the results.
- **Highest Quantity (hq)**: Identifies the product with the highest quantity and displays its details.

## Credits
Developed by [AntonioDiNics](https://github.com/AntonioDiNics).

