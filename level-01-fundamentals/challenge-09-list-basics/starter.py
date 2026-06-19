def get_first(lst):
    if len(lst) == 0:
        return None
    return lst[0]


def get_last(lst):
    if len(lst) == 0:
        return None
    return lst[-1]


def get_length(lst):
    return len(lst)


def add_item(lst, item):
    lst.append(item)
    return lst


def remove_item(lst, item):
    if item in lst:
        lst.remove(item)
    return lst


def sort_list(lst):
    return sorted(lst)


def sum_list(lst):
    return sum(lst)