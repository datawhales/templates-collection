from typing import Tuple
import numpy as np


# np.ones_like()
class OnesLikeArray:
    """Shape은 같고 1로 채워진 np.ndarray."""
    @staticmethod
    def ones_like():
        x = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
        
        # ones_like
        ret = np.ones_like(x)
        print(ret)
        return ret
    

# np.reshape()
class ReshapeArray:
    """Numpy array의 dimension은 변화 없이 shape을 변환."""
    @staticmethod
    def reshape():
        x = np.array([[1, 2], [3, 4]])

        # reshape
        ret = x.reshape((1, 4))
        print(ret)
        return ret

    @staticmethod
    def reshape_2():
        x = np.array([[1, 2], [3, 4]])

        # reshape
        ret = x.reshape((-1, 1))
        print(ret)
        return ret


# np.squeeze()
class SqueezeArray:
    """Numpy array의 single-dimension을 제거."""
    @staticmethod
    def squeeze():
        x = np.array([[1, 2, 3, 4]])

        # squeeze
        ret = x.squeeze(axis=0)
        print(ret)
        return ret

    @staticmethod
    def squeeze_2():
        x = np.array([[1], [2], [3], [4]])

        # squeeze
        ret = x.squeeze(axis=1)
        print(ret)
        return ret


if __name__ == "__main__":
    # np.ones_like()
    print(f"np.ones_like()")
    OnesLikeArray.ones_like()

    # np.reshape()
    print(f"np.reshape()")
    ReshapeArray.reshape()
    ReshapeArray.reshape_2()

    # np.squeeze()
    print(f"np.squeeze()")
    SqueezeArray.squeeze()
    SqueezeArray.squeeze_2()
