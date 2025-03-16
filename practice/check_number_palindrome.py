def is_palindrome(num):
    if num<0:
        return False

    reversed_number = 0
    original_num = num

    while num>0:
        rem = num%10
        reversed_number = reversed_number * 10 + rem
        num = num//10

    return reversed_number == original_num



def square_even_numbers(lst):
    # Using list comprehension to filter out even numbers and square them
    squared_evens = [x**2 for x in lst if x % 2 == 0]
    return squared_evens

# Example usage
#input_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
input_list = [-1, 2, -3, -4]
result_list = square_even_numbers(input_list)
print(result_list)

num = 122
if is_palindrome(num):
    print(f'{num} is palindrome')
else:
    print(f'{num} is not palindrome')