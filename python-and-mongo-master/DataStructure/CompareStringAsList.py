def compare(list1, list2):
    if list1 is None and list2 is None:
        return 0

    while list1 and list2 and list1.c == list2.c:
        list1 = list1.next
        list2 = list2.next

        # If either of the two lists has reached end
        if (list1 and not list2):
            return 1

        if (list2 and not list1):
            return -1

        if (list1 and list2):
            return 1 if list1.c > list2.c else -1

        return 0