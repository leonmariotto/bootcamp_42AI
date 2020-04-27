def ft_reduce(function_to_apply, list_of_inputs):
    n = list_of_inputs[0]
    if len(list_of_inputs) == 1:
        return n
    for index, elem in enumerate(list_of_inputs):
        n = function_to_apply(n, list_of_inputs[index + 1])
        if index >= len(list_of_inputs) - 2:
            break
    return n
