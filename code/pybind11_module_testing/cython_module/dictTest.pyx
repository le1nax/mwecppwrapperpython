cpdef dict manipulate_dict_cython(dict input_dict):
    cdef dict output_dict = {}
    for key, value in input_dict.items():
        output_dict[key] = value * 2
    return output_dict