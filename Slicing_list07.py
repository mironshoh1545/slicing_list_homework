def main(list1,n):
    """
    A list of several elements is given. Return all items from the beginning in n steps.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    
    n = []
    for i in  range(0, len(list1), n):
        n += [list1[i]]
    return n