from functools import reduce

def cumulative_sum(numbers):
    return reduce(lambda acc, num: acc + [acc[-1] + num], numbers[1:], [numbers[0]])

# Example usage:
numbers = [1, 2, 3, 4, 5]
cumulative_result = cumulative_sum(numbers)
print(cumulative_result)