from typing import Tuple
import numpy as np


# np.reshape()
def modify_dim(a: np.ndarray, shape: Tuple[int]) -> np.ndarray:
    ret = a.reshape(shape)
    return ret


def example():
    a = np.array([1, 2, 3, 4])
    b = modify_dim(a=a, shape=(1, 4))
    print(b)

if __name__ == "__main__":
    example()
