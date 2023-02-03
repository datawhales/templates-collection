from typing import Iterable, List, Tuple
import matplotlib.pyplot as plt

# TODO: plt 다양한 옵션 추가해서 최대한 많이 쓰는 옵션 다 넣기



font = {'family': 'serif',
        'color':  'darkred',
        'weight': 'normal',
        'size': 16,
        }


def plot_line_graph(x: List[int], y: List[int], figsize: Tuple[int, int]=(12, 4)) -> None:
    """두 변수에 대한 line graph를 그리는 함수."""
    plt.figure(figsize=figsize)

    plt.plot(x, y, color="red", label="Example Data")
    plt.xlabel("X Axis", fontsize=10)
    plt.ylabel("Y Axis", fontsize= 10)
    plt.axis([0, 5, 0, 15])  # X, Y 축 범위: [xmin, xmax, ymin, ymax]
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


def example():
    plt.figure(figsize=(12, 4))

    x = [1, 2, 3, 4]
    y = [2, 3, 5, 10]
    
    plt.plot(x, y, color="red", label="Example data")

    plt.xlabel("X Axis", fontsize=10)
    plt.ylabel("Y Axis", fontsize=10)
    plt.axis([0, 5, 0, 15])  # X, Y 축 범위: [xmin, xmax, ymin, ymax]
    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    example()
