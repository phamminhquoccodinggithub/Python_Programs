# To find the largest element in an array, iterate over each element and compare it with the current largest element. 
# If an element is greater, update the largest element. At the end of the iteration, the largest element will be found.

# Given an array, find the largest element in it.

# Input : arr[] = {10, 20, 4}
# Output : 20
# Input : arr[] = {20, 10, 20, 4, 100}
# Output : 100

def findLargestElement(arr):
    return max(arr)


def main():
    # Input array
    arr = list(map(int, input().split()))

    print("Result is %d" % findLargestElement(arr))

if __name__ == "__main__":
    main()