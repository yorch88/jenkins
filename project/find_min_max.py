def find_min_max_even(numbers):
    """Find the smallest and largest even numbers in a list."""
    evens = [num for num in numbers if num % 2 == 0]
    if not evens:
        raise ValueError("No even numbers found")
    return min(evens), max(evens)
