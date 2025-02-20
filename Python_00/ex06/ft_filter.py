
def ft_filter(function_to_apply, list_of_inputs):
    """
    ft_filter(function_to_apply, list_of_inputs) -> list

    Return a list of the elements that satisfy the condition of the function_to_apply.
    The function_to_apply should return a boolean value.
    """
    if (not callable(function_to_apply)):
        return list_of_inputs
    return [x for x in list_of_inputs if function_to_apply(x)]


if __name__ == '__main__':
    def is_even(x):
        return x % 2 == 0

    print(list(filter(None, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])))
    print(ft_filter(None, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))


