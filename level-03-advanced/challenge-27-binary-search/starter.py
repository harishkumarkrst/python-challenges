def binary_search_iterative(arr, target):
    """
    Iterative binary search.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


def binary_search_recursive(arr, target, low=0, high=None):
    """
    Recursive binary search.
    """
    if high is None:
        high = len(arr) - 1

    if low > high:
        return -1

    mid = (low + high) // 2

    if arr[mid] == target:
        return mid

    elif arr[mid] < target:
        return binary_search_recursive(
            arr, target, mid + 1, high
        )

    else:
        return binary_search_recursive(
            arr, target, low, mid - 1
        )


def find_insert_position(arr, target):
    """
    Find correct insertion index.
    """
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return low