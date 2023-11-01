def binary_search(lst, item):
    """
    A simple implementation of binary search for numeric collections.

    Time complexity:
        O(log(n))

    Args:
        lst: A sorted collection of numeric elements.
        item: A numeric element we are searching for.

    Returns:
        An index of searched element. None if not found.
    """

    low_idx = 0
    high_idx = len(lst) + 1

    while low_idx <= high_idx:  # Searching through collections of length >= 1

        mid_idx = (low_idx + high_idx) // 2
        guess = lst[mid_idx]

        if guess == item:
            return mid_idx
        elif guess < item:
            low_idx = mid_idx + 1
        else:
            high_idx = mid_idx - 1

    return None
