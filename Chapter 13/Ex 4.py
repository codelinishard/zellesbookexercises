def max(lst:list):
    if len(lst) == 0:
        raise ValueError("Empty list provided")
    if len(lst) == 1:
        return lst[0]
    largest = lst[0]
    next = max(lst[1:])
    if next > largest:
        largest = next
    return largest

