# Input : tuples = [(), ('ram','15','8′), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (”,”),()]
# Output : [('ram', '15', '8'), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (”, ”)]

# Input : tuples = [(”,”,'8′), (), ('0′, '00', '000'), ('birbal', ”, '45'), (”), (),  (”,”),()]
# Output : [(”, ”, '8'), ('0′, '00', '000'), ('birbal', ”, '45'), (”, ”)]

def removeEmpty(lst):
    newList = list(filter(None, lst))
    return newList

def main():
    lst = [(), ('ram', '15', '8'), (), ('laxman', 'sita'), ('krishna', 'akbar', '45'), (","), ()]
    print("Result is ", removeEmpty(lst))


if __name__ == "__main__":
    main()