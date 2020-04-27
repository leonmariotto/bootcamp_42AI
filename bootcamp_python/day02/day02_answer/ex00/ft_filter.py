def ft_filter(function_to_apply, list_of_inputs):
    for elem in list_of_inputs:
        if function_to_apply is None:
            if elem:
                yield elem
        elif function_to_apply(elem):
            yield elem
