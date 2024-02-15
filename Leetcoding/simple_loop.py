def print_sum_even_nums(even_nums):
    total = 0

    for x in even_nums:
        if x % 2 != 0:
            break

        total += x
    else:
        print("For loop executed normally")
        print(f'Sum of numbers {total}')


# this will print the sum
print_sum_even_nums([2, 4, 6, 8])

# this won't print the sum because of an odd number in the sequence
print_sum_even_nums([2, 4, 5, 8])

# Output

# For loop executed normally
# Sum of numbers 20