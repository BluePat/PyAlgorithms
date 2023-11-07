def selection_sort(arr):
    """
    A simple implementation of selection sort for numeric collections.

    Time complexity:
        O(n^2)

    Args:
        arr: A collection of numeric elements.

    Returns:
        A sorted collection of numeric elements.
    """

    def find_minimum(xs):
        idx = 0
        smallest_x = xs[0]

        for i, x in enumerate(xs):
            if x < smallest_x:
                smallest_x = x
                idx = i

        return idx

    sorted_arr = []

    for _ in range(len(arr)):
        idx_of_smallest = find_minimum(arr)
        sorted_arr.append(arr.pop(idx_of_smallest))

    return sorted_arr
