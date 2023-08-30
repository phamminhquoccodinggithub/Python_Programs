# Given a list of integers with duplicate elements in it. The task is to generate another list,
# which contains only the duplicate elements. In simple words, the new list should contain elements that appear as more than one.

# Examples:

# Input : list = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
# Output : output_list = [20, 30, -20, 60]
# Input :  list = [-1, 1, -1, 8]
# Output : output_list = [-1]

from collections import Counter

def findDuplicates(lst):
    count = Counter(lst)
    return list(i[0] for i in count.items() if i[1] > 1)

def main():
    lst = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
    print("Result is ", findDuplicates(lst))


if __name__ == "__main__":
    main()