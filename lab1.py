
def max_list_iter(int_list):  # must use iteration not recursion
    """finds the max of a list of numbers and returns the value (not the index)
    If int_list is empty, returns None. If list is None, raises ValueError"""
    if int_list == []:
        return None
    elif int_list is None:
        raise ValueError
    max_val = int_list[0]
    for i in range(len(int_list)):
        if max_val < int_list[i]:
            max_val = int_list[i]
    return max_val


def reverse_rec(int_list):   # must use recursion
    """recursively reverses a list of numbers and returns the reversed list
    If list is None, raises ValueError"""
    if int_list is None:
        raise ValueError
    if int_list == []:
        return []
    return reverse_rec(int_list[1:]) + [int_list[0]]


def bin_search(target, low, high, int_list):  # must use recursion
    """searches for target in int_list[low..high] and returns index if found
    If target is not found returns None. If list is None, raises ValueError """
    if int_list is None:
        raise ValueError

    if high < low:
        return None

    mid = (high + low)//2
    if int_list[mid] == target:
        return mid
    elif int_list[mid] > target:
        return bin_search(target, low, mid-1, int_list)
    elif int_list[mid] < target:
        return bin_search(target, mid+1, high, int_list)

