
def shifting_range(numpy_arr):
    import numpy as np
    input_arr = numpy_arr
    print(f"{np.roll(input_arr, 1)}")
    output_arr = input_arr - np.roll(input_arr, 1)  # subtração de vetores
    return output_arr