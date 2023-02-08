import numpy as np
import pandas as pd


# df.rolling
def rolling_df(df: pd.DataFrame, window: int) -> pd.DataFrame:
    """데이터프레임을 입력 받아 rolling을 수행하고 결과 데이터프레임을 반환하는 함수."""
    rolled_df = df.rolling(
        window=window,
        min_periods=None,
        center=False,
        win_type=None,
        on=None,
        axis=0,
        closed=None,
        step=None,
        method="single",
    )
    return rolled_df


def example():
    df = pd.DataFrame({"A": [0, 1, 2, np.nan, 4]},
        index=[
            pd.Timestamp('20130101 09:00:00'),
            pd.Timestamp('20130101 09:00:02'),
            pd.Timestamp('20130101 09:00:03'),
            pd.Timestamp('20130101 09:00:05'),
            pd.Timestamp('20130101 09:00:06'),
        ]
    )

    rolled_df = df.rolling(window="2s").sum()
    display(rolled_df)


if __name__ == "__main__":
    example()
