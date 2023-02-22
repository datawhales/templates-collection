import pandas as pd
import numpy as np


class FillNanValues:
    """Dataframe의 nan 값 채우기."""
    @staticmethod
    def example():
        df = pd.DataFrame([[1, 2, 2],
                           [1, 2, 2],
                           [2, np.nan, 2],
                           [3, 3, np.nan],
                           [np.nan, 5, 5]])

        # 1. 특정 값으로 fill
        df_1 = df.fillna(value=0)

        # 2. 인접한 행의 값으로 fill (ffill, bfill)
        df_2 = df.fillna(method="ffill")

        # 3. 각 열의 평균값으로 fill (최솟값, 최댓값의 경우 df.min(), df.max() 사용)
        df_3 = df.fillna(df.mean())

        # 4. 각 열의 most frequent 값으로 fill
        df_4 = df.fillna(df.mode().iloc[0])
        
        # 5. 각 행의 평균값으로 fill
        df_5 = df.T.fillna(df.T.mean()).T

        # 6. 각 행의 most frequent 값으로 fill
        df_6 = df.T.fillna(df.T.mode().iloc[0]).T
        
        # 7. Interpolation
        df_7 = df.interpolate()
