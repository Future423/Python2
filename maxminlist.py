def find_max_min(input_list):
    if not input_list:
        return None, None  # Return None for both max and min if the list is empty

    # Initialize max and min with the first element of the list
    max_value = input_list[0]
    min_value = input_list[0]

    # Traverse the list to find the maximum and minimum values
    for num in input_list:
        if num > max_value:
            max_value = num
        elif num < min_value:
            min_value = num

    return max_value, min_value

# Example usage:
if __name__ == "__main__":
    numbers = [12, 45, 67, 89, 34, 23, 9]
    max_num, min_num = find_max_min(numbers)
    
    if max_num is not None and min_num is not None:
        print(f"Maximum value: {max_num}")
        print(f"Minimum value: {min_num}")
    else:
        print("The list is empty.")
