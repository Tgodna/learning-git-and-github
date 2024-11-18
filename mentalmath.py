numbers = [57, 10, 82, 36, 89, 46, 13, 23, 92, 48]
even = []
for num in numbers:
    even.append(num % 2 == 0)

even_numbers = [num for num in numbers if num % 2 == 0]

print('Original Numbers:', numbers)
print('Even numbers:', list(even_numbers))