# Given an array of integers, find the sum of its elements.

# Examples:

# Input : arr[] = {1, 2, 3}
# Output : 6
# Explanation: 1 + 2 + 3 = 6

def findSumOfArray(arr):
    return sum(arr)

def main():
    # Input array
    arr = list(map(int, input().split()))

    print("Result is %d" % findSumOfArray(arr))

if __name__ == "__main__":
    main()
