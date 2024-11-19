def rotate_array(arr, k):
    n = len(arr)
    k = k % n  # Handle cases where k > n
    return arr[-k:] + arr[:-k]

# Example
array = [1, 2, 3, 4, 5, 6]
k = 2
rotated_array = rotate_array(array, k)
print("Original array:", array)
print("Rotated array:", rotated_array)
