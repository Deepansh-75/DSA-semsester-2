def find_max_min(arr):
    if not arr:
        return None, None

    # Initialize with the first element
    max_val = arr[0]
    min_val = arr[0]

    # Iterate through the array once
    for num in arr:
        if num > max_val:
            max_val = num
        elif num < min_val:
            min_val = num
            
    return max_val, min_val

# Example usage:
numbers = [34, 7, 23, 32, 5, 62]
max_num, min_num = find_max_min(numbers)

print(f"Maximum: {max_num}")
print(f"Minimum: {min_num}")