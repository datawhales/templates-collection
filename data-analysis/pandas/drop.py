from typing import List
import numpy as np
import pandas as pd
from IPython.display import display

# df.dropna
def drop_by_col(df: pd.DataFrame, col_list: List[str]) -> pd.DataFrame:
    """특정 column의 값이 nan인 row들을 drop하는 함수."""
    filtered_df = df.dropna(
        axis=0,  # 0이면 drop row, 1이면 drop column
        how="any",  # any이면 nan인 값이 하나라도 있으면 drop, all이면 모두 nan일 때 drop
        subset=col_list,  # nan인지 확인하고자 하는 column 리스트
        inplace=False,
    )
    return filtered_df


def example():
    df = pd.DataFrame({
        "A": [1, 2, 3, 4, None],
        "B": [None, 2, 3, None, 5],
        "C": [6, 7, 8, 9, 10]
    })

    display(df)

    filtered_df = df.dropna(subset=["A", "B"])

    display(filtered_df)


if __name__ == "__main__":
    example()
