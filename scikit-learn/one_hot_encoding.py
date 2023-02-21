import pandas as pd
import numpy as np


# sklearn.preprocessing.OneHotEncoder
# https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html
class OneHotEncoding:
    """One-hot encoding을 통해 데이터 변환."""
    @staticmethod
    def example():
        from sklearn.preprocessing import OneHotEncoder

        df = pd.DataFrame([["A", 18], ["A", 17], ["B", 16], ["C", 19], ["C", 18]],
                          columns=["Grade", "Age"])

        ohe = OneHotEncoder(sparse=False)

        # One hot encoding to "Grade" column
        one_hot_encoded = ohe.fit_transform(df["Grade"].values.reshape(-1, 1))

        # One hot encoded dataframe
        new_df = pd.DataFrame(one_hot_encoded, columns=[f"Grade_{x}" for x in ohe.categories_[0]])

        return pd.concat([df.drop(columns="Grade"), new_df], axis=1)
        


if __name__ == "__main__":
    # sklearn.preprocessing.OneHotEncoder
    print("sklearn.preprocessing.OneHotEncoder")
    print(OneHotEncoding.example())
