def is_zero(nums):
    return sum(nums) == 0

def calc_squares(nums):
    return [num**2 for num in nums]

def start():
    numbers = []
    while True:
        number = float(input("Enter a number: "))
        numbers.append(number)
        if is_zero(numbers):
            return calc_squares(numbers)

if __name__ == '__main__':
    print(start())