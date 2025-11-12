import numpy as np

if __name__ == "__main__":
    array = np.array([0, 0, 0])
    print(array == 0)
    print(array[:] == 0, end="\n\n")

    array2d = np.array([[0, 0, 0],  # 0 0
                      [0, 0, 0]])   # 0 0
                                    # 0 0
    print(array2d == 0)
    print(array2d[1, :] == 0)
    print(array2d[1, :] == [0, 0, 0], end="\n\n")

    print(np.all(array2d[1, :] == 0))
    print(np.all(array2d[1, :] == [0, 0, 0]), end="\n\n")

    # How numpy comparison works 

    array_class = type(array2d)
    print(f"The class is: {array_class}")

    # Show the __eq__ method that *belongs* to this class
    print(f"The __eq__ method is: {array_class.__eq__}")

    # https://github.com/numpy/numpy/blob/main/numpy/_core/src/multiarray/arrayobject.c (line 823)
    # https://numpy.org/doc/2.3/reference/generated/numpy.equal.html
    # https://numpy.org/doc/stable/user/basics.broadcasting.html
