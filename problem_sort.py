def selection_sort(arr):

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
