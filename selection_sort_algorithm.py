"""Selection Sort Algorithm Implementation"""
def selection_sort(arr):
    """Function to perform selection sort on a list of numbers."""
    # Outer loop: position where the next smallest element should go
    for i, _ in enumerate(arr):
        min_index = i

        # Inner loop: find index of smallest element in the rest of the list
        for j, value in enumerate(arr[i+1:], start=i+1):
            if value < arr[min_index]:
                min_index = j

        # Swap the smallest found into position i
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

print(selection_sort([33, 1, 89, 2, 67, 245]))
print(selection_sort([5, 16, 99, 12, 567, 23, 15, 72, 3]))
