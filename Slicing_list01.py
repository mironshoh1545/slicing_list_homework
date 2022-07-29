
def main(numbers):
    """
    A list called numbers is given. Return the items in the odd index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    n = []
    for i in  range(0, len(numbers), 2):
        n += [numbers[i]]
    return n 