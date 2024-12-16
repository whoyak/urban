def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        results[func.__name__] = (func(int_list))
    return results


def minn(numbers):
    return min(numbers)


def maxx(numbers):
    return max(numbers)


def lenn(numbers):
    return len(numbers)


def summ(numbers):
    return sum(numbers)


def sortedd(numbers):
    return sorted(numbers)


print(apply_all_func([6, 20, 15, 9], maxx, minn))
print(apply_all_func([6, 20, 15, 9], lenn, summ, sortedd))
