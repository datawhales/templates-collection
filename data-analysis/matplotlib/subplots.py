import matplotlib.pyplot as plt


def plot_subgraphs():
    pass
    # fig, ax = plt.subplots(figsize=(30, 5))
    # ax.scatter(train_score.index, train_score.rolling(rolling_window).agg("mean"), color="C0", s=1, alpha=0.6, label="Train")
    # ax.scatter(valid_score.index, valid_score.rolling(rolling_window).agg("mean"), color="C1", s=1, alpha=0.6, label="Valid")
    # ax.scatter(test_score.index, test_score.rolling(rolling_window).agg("mean"), color="C2", s=1, alpha=0.6, label="Test")
    # ax.axvline(warning_1, color="orange")
    # ax.axvline(warning_2, color="orange")
    # ax.axvline(pm, color="red")
    # ax.axhline(threshold, color="red", linestyle='--', alpha=0.5)
    # ax.axvspan(warning_1 - pd.to_timedelta("2D"), warning_1, facecolor="red", alpha=0.3)
    # ax.axvspan(warning_2 - pd.to_timedelta("2D"), warning_2, facecolor="red", alpha=0.3)
    # ax.axvspan(pm, pm + pd.to_timedelta("2D"), facecolor="blue", alpha=0.3)
    # ax.legend()
    # plt.title("Anomaly-score")
    # plt.show()


def example():
    pass


if __name__ == "__main__":
    example()
