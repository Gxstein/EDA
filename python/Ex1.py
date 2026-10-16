# Exercise 01 — Working with Lists

numbers = [10, 25, 3, 42, 18]

largest = numbers[0]
smallest = numbers[0]
total = 0

for number in numbers:
    if number > largest:
        largest = number

    if number < smallest:
        smallest = number

    total += number

print("Numbers:", numbers)
print("Largest number:", largest)
print("Smallest number:", smallest)
print("Sum:", total)
