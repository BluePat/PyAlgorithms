import problem_search as search
import problem_sort as sort

if __name__ == '__main__':

    # Simple numeric BINARY SEARCH
    lst = [1, 2, 5, 50, 60, 61, 63, 69, 74, 84, 90, 95, 99, 101]
    results = [search.binary_search(lst, elem) for elem in lst]
    print(results)

    # Simple numeric SELECTION SORT
    lst = [50, 30, 30, 40, 123, 12, 34, 56, 55, 55, 2, 888, 14, 15, 1, 0]
    result = sort.selection_sort(lst)
    print(result)

    # Simple numeric QUICKSORT
    lst = [50, 30, 30, 40, 123, 12, 34, 56, 55, 55, 2, 888, 14, 15, 1, 0]
    result = sort.quicksort(lst)
    print(result)
