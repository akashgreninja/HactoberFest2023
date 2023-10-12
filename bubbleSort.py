def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

# Input from the user
input_str = input("Enter a list of numbers separated by spaces: ")
user_input = [int(x) for x in input_str.split()]

# Sort the user's input
bubble_sort(user_input)

# Display the sorted list
print("Sorted list is:", user_input)
