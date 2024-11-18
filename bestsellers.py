import csv

# Initialize the variables
max_sales = 0
best_selling_book = ""

# Open the CSV file for reading
with open('bestsellers.csv', 'r', encoding='utf-8') as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header row
    
    # Loop through the rows to find the book with max sales
    for row in reader:
        current_sales = float(row[4])  # Assuming sales are in the 5th column (index 4)
        
        if current_sales > max_sales:
            max_sales = current_sales
            best_selling_book = row[0]  # Assuming book name is in the 1st column (index 0)

# Output the result
print(f"The best-selling book is: {best_selling_book} with {max_sales} million sales.")

# Open the file again to overwrite with new header
with open('bestsellers.csv', 'w', newline='', encoding='utf-8') as file:
    csv_writer = csv.writer(file)
    
    # Write a new header and the best-selling book information
    csv_writer.writerow(['Book', 'Author', 'Sales in Millions'])
    csv_writer.writerow([best_selling_book, 'Author Name', max_sales])  # Replace 'Author Name' with actual author if available
