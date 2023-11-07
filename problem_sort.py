from random import randrange

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


def quicksort(xs):
    """
        A simple implementation of quicksort for numeric collections.
        Good introductory example for D&C algorithms.

        Time complexity:
            The worst case: O(n^2)
            The average case: O(n*log(n))

            Average case can be achieved constantly by selecting pivots at random.

        Args:
            xs: A collection of numeric elements.

        Returns:
            A sorted collection of numeric elements.
        """

    if len(xs) < 2:
        return xs

    pivot_idx = randrange(0, len(xs))
    pivot = xs.pop(pivot_idx)

    left_array, right_array = [], []
    for x in xs:
        if x < pivot:
            left_array.append(x)
        else:
            right_array.append(x)

    return quicksort(left_array) + [pivot] + quicksort(right_array)
