import csv  # Ensure the CSV module is imported.

data = [
    ['Item', 'Quantity'],
    ['Blender', 2],
    ['Posters', 30],
    ['Shoes', 2]
]

# Define the correct file path, here using 'packing_list.csv'
filename = 'packing_list.csv'

try:
    # Try to open the file for reading
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)  # Print rows from the existing CSV file
except FileNotFoundError:
    # If the file doesn't exist, create a new file and write data to it
    print('Packing list file not found. Creating a new one.')
    
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)  # Write the initial data to the new file
