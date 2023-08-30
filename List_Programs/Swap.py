# Given a list in Python and provided the positions of the elements, write a program to swap the two elements in the list.

# Examples:

# Input : List = [23, 65, 19, 90], pos1 = 1, pos2 = 3
# Output : [19, 65, 23, 90]

# Input : List = [1, 2, 3, 4, 5], pos1 = 2, pos2 = 5
# Output : [1, 5, 3, 4, 2]

def swapPosition(lst, pos1, pos2):
    """
        @note: swap positions of the elements in list
        @param lst: list of numbers
        @param pos1, pos2: position os the element to swap
    """
    lst[pos1], lst[pos2] = lst[pos2], lst[pos1]
    return lst


def main():
    lst = [1, 2, 3, 4, 5]
    pos1 = 2
    pos2 = 5
    print("List before swap: ", lst)
    print("Swap postion %s and position %s" % (pos1, pos2))
    print("Result is ", swapPosition(lst, pos1-1, pos2-1))


if __name__ == "__main__":
    main()
