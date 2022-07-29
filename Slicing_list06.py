def main(list1):
    """A list of several elements is given. Return all items from the beginning in three steps.
    Args:
        list1(list): parameter
    Returns:
        list: return answer.
    """
 
    n = []
    for i in  range(0, len(list1), 3):
        n += [list1[i]]
    return n