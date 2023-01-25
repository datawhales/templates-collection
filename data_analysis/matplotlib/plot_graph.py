import matplotlib.pyplot as plt

# TODO: plt 다양한 옵션 추가해서 최대한 많이 쓰는 옵션 다 넣기
def main():
    plt.plot([1, 2, 3, 4], [2, 3, 5, 10], color="red", label="Example Data")
    plt.xlabel("X Axis", fontsize=10)
    plt.ylabel("Y Axis", fontsize= 10)
    plt.axis([0, 5, 0, 15])  # X, Y 축 범위: [xmin, xmax, ymin, ymax]
    plt.legend()
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
