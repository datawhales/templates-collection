import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def draw_heatmap():
    """Heatmap 그리는 함수."""
    df = pd.DataFrame(np.random.randn(50).reshape(10, 5))
    corr = df.corr()

    # data 를 제외한 모든 argument 는 default 값
    # https://seaborn.pydata.org/generated/seaborn.heatmap.html
    ax = sns.heatmap(
        data=corr,
        vmin=None,
        vmax=None,
        cmap=None,
        center=None,
        robust=False,
        annot=None,
        fmt=".2g",
        annot_kws=None,
        linewidths=0,
        linecolor="white",
        cbar=True,
        cbar_kws=None,
        cbar_ax=None,
        square=False,
        xticklabels="auto",
        yticklabels="auto",
        mask=None,
        ax=None,
    )

    plt.show()


def show_example():
    df = pd.DataFrame(np.random.randn(50).reshape(10, 5))
    corr = df.corr()

    ax = sns.heatmap(
        data=corr,
        vmin=0,
        vmax=1,
        cmap="Blues",
        linewidths=2,
        cbar=True,
        square=True,
        xticklabels=["a", "b", "c", "d", "e"],
        yticklabels=["A", "B", "C", "D", "E"],
    )

    plt.show()


def show_example_2():
    fig, axes = plt.subplots(1, 2, sharey=True, figsize=(12, 5))  # fig 는 전체 subplot, axes 는 각각의 subplot
    
    df1 = pd.DataFrame(np.random.randn(50).reshape(10, 5))
    df2 = pd.DataFrame(np.random.randn(50).reshape(10, 5))

    for df, ax in zip([df1, df2], axes):
        cbar_ax = fig.add_axes([1.02, 0.05, 0.02, 0.85])   # 상대 위치 지정: [left, bottom, width, height]
        
        sns.set(font_scale=1)
        
        sns.heatmap(
            data=abs(df.corr()),
            vmin=0.2,
            vmax=1,
            cmap="Blues",
            annot=False,
            cbar=True,
            cbar_ax=cbar_ax,
            xticklabels=False,
            yticklabels=["A", "B", "C", "D", "E"],
            ax=ax,
        )
    
    plt.show()


def main():
    print("Default:\n")
    draw_heatmap()
    print("Example 1:\n")
    show_example()
    print("Example 2:\n")
    show_example_2()


if __name__ == "__main__":
    main()
