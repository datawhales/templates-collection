from sklearn.preprocessing import StandardScaler, MinMaxScaler
import numpy as np


# sklearn.preprocessing.StandardScaler
class StandardScaling:
    """StandardScaler 적용하는 예시"""
    @staticmethod
    def scale():
        X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        X_test = np.array([[2, 4, 6], [5, 7, 9]])

        scaler = StandardScaler()

        # X_train에 맞는 스케일러로 변형
        X_train_scaled = scaler.fit_transform(X_train)

        # X_test에도 해당 스케일러를 적용
        X_test_scaled = scaler.transform(X_test)

        print(X_train_scaled)
        print(X_test_scaled)
        return X_train_scaled, X_test_scaled


# sklearn.preprocessing.MinMaxScaler
class MinMaxScaling:
    """MinMaxScaler 적용하는 예시"""
    @staticmethod
    def scale():
        X_train = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        X_test = np.array([[2, 4, 6], [5, 7, 9]])

        scaler = MinMaxScaler()

        # X_train에 맞는 스케일러로 변형
        X_train_scaled = scaler.fit_transform(X_train)

        # X_test에도 해당 스케일러를 적용
        X_test_scaled = scaler.transform(X_test)

        print(X_train_scaled)
        print(X_test_scaled)
        return X_train_scaled, X_test_scaled


if __name__ == "__main__":
    # sklearn.preprocessing.StandardScaler
    print("sklearn.preprocessing.StandardScaler")
    StandardScaling.scale()

    # sklearn.preprocessing.MinMaxScaler
    print("sklearn.preprocessing.MinMaxScaler")
    MinMaxScaling.scale()
