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

# https://stackoverflow.com/questions/10580676/comparing-two-numpy-arrays-for-equality-element-wise
