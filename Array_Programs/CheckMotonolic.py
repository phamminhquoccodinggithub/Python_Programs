# Given an array A containing n integers. The task is to check whether the array is Monotonic or not.
# An array is monotonic if it is either monotone increasing or monotone decreasing.
# An array A is monotone increasing if for all i <= j, A[i] <= A[j].

# An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

# Return Type: Boolean value, “True” if the given array A is monotonic else return “False” (without quotes).

# Examples:

# Input : 6 5 4 4
# Output : true

# Input : 5 15 20 10
# Output : false

def isMonotonic(arr):
    return all(arr[i] >= arr[i+1] for i in range(1, len(arr)-1)) or \
        all(arr[i] <= arr[i+1] for i in range(1, len(arr)-1))


def main():
    # Input array
    arr1 = [5, 15, 20, 10]
    arr2 = [6, 5, 4, 4]
    arr3 = [1, 2, 3, 4, 5]  # True
    arr4 = [5, 4, 3, 2, 1]  # True
    arr5 = [1, 2, 2, 3, 4]  # True
    arr6 = [1, 2, 3, 4, 5, 4]  # False

    print(isMonotonic(arr1))  # should return False
    print(isMonotonic(arr2))  # should return True
    print(isMonotonic(arr3))  # should return True
    print(isMonotonic(arr4))  # should return True
    print(isMonotonic(arr5))  # should return True
    print(isMonotonic(arr6))  # should return False


if __name__ == "__main__":
    main()
