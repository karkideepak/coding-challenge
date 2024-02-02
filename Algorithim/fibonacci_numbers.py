# Recurisve Computations
"""
Recursion occurs when a function is defined using computations that involve invoking itself with different arguments.

Consider N!, which is the factorial of the integer N. This value is the product of all positive integers less than or equal to N.Thus, 
5!=5x4x3x2x1 = 120. 

Another way to represent these operations is to define the function recursively. You might be able to see that 

N!=N x (N-1)!

For example, 
4! = 4x3x2x1 = 24, and this confirms that 
5! = 120 =5 x4!
"""

# Each recursive function has a base case that eventually ensures the recursion stops. Here, fact(1) will return 1 and invoke fact(). 

"""
As an added security protection if, fact(N) is called with any integer less than or equal to 1, fact() will return the value 1.

def fact(N):
	# Base Case
	if N <= 1:
		return 1

	# Recursive case
	return N * fact(N-1)
# In the recursive case, fact(N) call itself with an argument of (N-1) and multiplies the returned computation by N to produce the final result
"""

if __name__ == '__main__':
	import timeit
	import decimal
	print('N Time Fact(N)')

	for N in range(10, 200, 10):
		elapsed = timeit.timeit('fact(N)', globals=globals(), number=1000)
		d = decimal.Decimal(fact(N))
		print(f'{N:3d} {elapsed:.3f} {d:.6e})