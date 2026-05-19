import sys

# Merge sort with inversion count
def merge_sort_and_count(arr):
    """ Function to sort the array and count inversions using merge sort. """
    if len(arr) < 2:
        return arr, 0

    mid = len(arr) // 2
    left, left_inv = merge_sort_and_count(arr[:mid])
    right, right_inv = merge_sort_and_count(arr[mid:])
    
    merged, split_inv = merge_and_count(left, right)
    
    return merged, left_inv + right_inv + split_inv

def merge_and_count(left, right):
    """ Merge two sorted arrays and count the number of split inversions. """
    i = j = 0
    merged = []
    inv_count = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv_count += len(left) - i  # All remaining elements in left are greater than right[j]

    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged, inv_count

def count_inversions(arr):
    """ Wrapper function to initiate merge sort and count inversions. """
    _, inv_count = merge_sort_and_count(arr)
    return inv_count

def main():
    # Simulate input when running in Spyder
    if 'SPYDER' in sys.modules:
        input_data = """2

3
3
1
2

5
2
3
8
6
1
"""
        # Splitting the input data into lines
        data = input_data.splitlines()
    else:
        data = sys.stdin.read().splitlines()

    # Ensure input lines are read correctly and handle them safely
    i = 0
    if not data or len(data) == 0:
        print("No input provided!")
        return

    t = int(data[i].strip())  # Number of test cases
    i += 1
    results = []
    
    while i < len(data):
        if data[i].strip() == "":  # Handle the blank line between test cases
            i += 1
            continue
        
        # Read the size of the array
        n = int(data[i].strip())
        i += 1

        # Read the array elements
        arr = []
        for _ in range(n):
            arr.append(int(data[i].strip()))
            i += 1
        
        # Process the array to count inversions
        results.append(str(count_inversions(arr)))

        # Skip the blank line after the array
        if i < len(data) and data[i].strip() == "":
            i += 1

    # Output all results
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
