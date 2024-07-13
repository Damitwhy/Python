numbers = [12, 45, 60, 87, 999, 200, 84, 42, 87, 77, 2, 3, 77, 99, 20]
numbers = sorted(numbers)
def get_odd_numbs(nums):
    odd_numbers = []
    for number in nums:
        if number % 2 != 0:
            odd_numbers.append(number)
    return odd_numbers
result = get_odd_numbs(numbers)
print(result)

print(numbers)

class HelloWorld:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'Hello, world!'
    
HelloWorld

def fizzbuzz(start, end):
    return "\n".join(["FizzBuzz" if i % 3 == 0 and i % 5 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i) for i in range(start, end + 1)])

# Get input from the user
start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))

# Print the FizzBuzz result for the given range
print(fizzbuzz(start, end))