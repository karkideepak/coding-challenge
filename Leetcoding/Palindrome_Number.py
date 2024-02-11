# Palindrome number
"""
Given an integer x, return true if x is a palindrome and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""

"""
Lets take a input from the user, and save it to the variable S.
Any characters or numbers passed by user is saved as string.

# lets create a condtion to save the reverse values

Using the slicing method

#slicing the entire strings, not specyfying the starting and ending
# -1 indicates we want to step back and store the values in variable reverse

Check weather the orginal value is equal the reverse
if its the values are planidrome
"""
# Solution 1
"""
s = input("Enter the value: ")
reverse = s[::-1]
if (s == reverse):
    print("True, palindrome")

if (s != reverse):
    print("False, not palindrome")
"""
# Solution 2
"""
def Solution():
    x = input("Enter numbers or characters: ")
    isPalindrome = x[::-1]

    if x == isPalindrome:
        print(f"{x} is a palindrome")
    else:
        print(f"{x} is not a palindrome")

Solution()
"""
# Soltuion 3
class Solution():
    def isPalindrome(self, x):
        s = str()
        return s == s[::-1]
# Solution 4
"""
class Solution:
    def isPalindrome(self, x):
        y = x[::-1]
        if x == y:
            print("True")
        else:
            print("False")

# Create an instance of the class
solution_instance = Solution()

# Call the method on the instance and pass a value
solution_instance.isPalindrome(input("Enter a number: "))

"""
def Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        if x==0:
            return True
        if x%10 == 0:
            return False
        originalX =x
        numReversed = 0
        
        while x > 0:
            lastDigit = x%10
            numReversed = numReversed * 10 + lastDigit
            x= x//10
        
        return numReversed == originalX
    
