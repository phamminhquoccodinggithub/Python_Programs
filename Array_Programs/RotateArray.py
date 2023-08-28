# Write a function rotate(arr[], d, n) that rotates arr[] of size n by d elements. 

# Input arr[] = [1, 2, 3, 4, 5, 6, 7], d = 2, n = 7
# Array after left rotation is:  [3, 4, 5, 6, 7, 1, 2]

def rotateArray(arr, d):
    newArr = arr[d:] + arr[:d]
    return newArr

def main():
    # Input array
    arr = list(map(int, input().split()))
    d = 2
    print("Result is ", rotateArray(arr, d))

if __name__ == "__main__":
    main()
