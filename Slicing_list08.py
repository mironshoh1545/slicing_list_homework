def main(list1,n):
    """
    A list of several elements is given. Return all items from end n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """ 
    list1 = list1[::-1]
    n = []
    for i in  range(0, len(list1), n):
        n += [list1[i]]
    return n
    return 