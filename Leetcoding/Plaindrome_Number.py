# Plaindrome number
"""
Given an integer x, return true if x is a palindrome and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""
s = input("Enter the value: ")
"""
Lets take a input from the user, and save it to the variable S.
Any characters or numbers passed by user is saved as string.
"""
# lets create a condtion to save the reverse values
"""
Using the slicing method
"""
reverse = s[::-1]
#slicing the entire strings, not specyfying the starting and ending
# -1 indicates we want to step back and store the values in variable reverse
"""
Check weather the orginal value is equal the reverse
if its the values are planidrome
"""
if (s == reverse):
    print("True, palindrome")

if (s != reverse):
    print("False, not palindrome")




