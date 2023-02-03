from typing import Tuple
import numpy as np


# np.reshape()
def reshape(x: np.ndarray, shape: Tuple[int]) -> np.ndarray:
    """Numpy array의 dimension은 변화 없이 shape을 변환하는 함수."""
    ret = x.reshape(shape)
    return ret


# np.squeeze()
def squeeze(x: np.ndarray, axis: int = 0) -> np.ndarray:
    """Numpy array의 single-dimension을 제거하는 함수."""
    ret = x.squeeze(axis=axis)
    return ret


def example():
    a = np.array([[1, 2], [3, 4]])

    # reshape
    b = a.reshape((1, 4))
    print(f"b: {b}")

    # reduce dimension
    c = b.squeeze(axis=0)
    print(f"c: {c}")


def example_2():
    a = np.array([[1, 2], [3, 4]])

    # reshape
    b = a.reshape((-1, 1))
    print(f"b: {b}")

    # reduce dimension
    c = b.squeeze(axis=1)
    print(f"c: {c}")


if __name__ == "__main__":
    print("Example 1:")
    example()
    print("\nExample 2:")
    example_2()
