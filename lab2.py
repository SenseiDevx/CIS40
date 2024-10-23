"""
CIS 40 Lab 2
"""

# Exercise 2.2, Problem 2

# Ask the user for the price of the book and the number of copies
book_price = float(input("Enter the price of the book: "))
num_books = int(input("Enter the number of books: "))

# Define the bookstore discount and shipping costs
discount_rate = 0.40
first_copy_shipping = 3.00
additional_copy_shipping = 0.75

# Calculating the discounted price
discounted_price = book_price * (1 - discount_rate)

# Total cost calculation
total_book_cost = discounted_price * num_books
total_shipping_cost = first_copy_shipping + additional_copy_shipping * (num_books - 1)
total_cost = total_book_cost + total_shipping_cost

# Printing the result
print(f"The total cost for {num_books} books is: {total_cost:.2f}")

# Execution and output Exercise 2.2, Problem 2
"""
Enter the price of the book: 25.50
Enter the number of books: 60
The total cost for 60 books is: 965.25
"""



# Exercise 2.2, Problem 3

# Prompting user input for the starting time
start_hour = int(input("Enter Starting Hour: "))
start_minute = int(input("Enter Starting Minute: "))

# Time taken for each mile
easy_pace_min = 8
easy_pace_sec = 15
tempo_pace_min = 7
tempo_pace_sec = 12

# Total time in seconds
total_seconds = (1 * (easy_pace_min * 60 + easy_pace_sec)) + \
                (3 * (tempo_pace_min * 60 + tempo_pace_sec)) + \
                (1 * (easy_pace_min * 60 + easy_pace_sec))

# Converting the total seconds to minutes and hours
total_minutes = total_seconds // 60
total_seconds = total_seconds % 60
end_minute = (start_minute + total_minutes) % 60
end_hour = start_hour + (start_minute + total_minutes) // 60

# Printing the results
print(f"You will finish at {end_hour}:{end_minute:02d}")

# Execution and output Exercise 2.2, Problem 3
"""
Enter Starting Hour: 6
Enter Starting Minute: 52
You will finish at 7:30
"""