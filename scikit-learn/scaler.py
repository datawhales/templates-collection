import numpy as np


# sklearn.preprocessing.StandardScaler
class StandardScaling:
    """StandardScaler 적용하는 예시"""
    @staticmethod
    def example():
        from sklearn.preprocessing import StandardScaler

        X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        X_test = np.array([[2, 4, 6], [5, 7, 9]])

        scaler = StandardScaler()

        # X_train에 맞는 스케일러로 변형
        X_train = scaler.fit_transform(X_train)

        # X_test에도 해당 스케일러를 적용
        X_test = scaler.transform(X_test)

        return X_train, X_test


# sklearn.preprocessing.MinMaxScaler
class MinMaxScaling:
    """MinMaxScaler 적용하는 예시"""
    @staticmethod
    def example():
        from sklearn.preprocessing import MinMaxScaler

        X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        X_test = np.array([[2, 4, 6], [5, 7, 9]])

        scaler = MinMaxScaler()

        # X_train에 맞는 스케일러로 변형
        X_train = scaler.fit_transform(X_train)

        # X_test에도 해당 스케일러를 적용
        X_test = scaler.transform(X_test)

        return X_train, X_test


if __name__ == "__main__":
    # sklearn.preprocessing.StandardScaler
    print("sklearn.preprocessing.StandardScaler")
    print(StandardScaling.example())

    # sklearn.preprocessing.MinMaxScaler
    print("sklearn.preprocessing.MinMaxScaler")
    print(MinMaxScaling.example())
