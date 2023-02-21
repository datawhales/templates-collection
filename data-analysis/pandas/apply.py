# Example
# BURST_N_COLS = 4096


# def acc2vel(
#     data: pd.Series, sr: int = 8192, n_samples: int = 4096, use_eps: bool = True,
# ) -> pd.Series:
#     """Get burst velocity data from burst acceleration data.

#     Args:
#         data (pd.Series): Input series(Burst acceleration data).
#         sr (int): Sample rate.
#         n_samples (int): Number of samples.
#         use_eps (bool): Whether to use error correction.

#     Returns:
#         (pd.Series): Burst velocity data.
#     """
#     # Error correction
#     if use_eps:
#         eps = data.sum() / n_samples
#         data -= eps

#     data = data.cumsum()

#     first_data = data.iloc[0]
#     data = data.rolling(window=2).sum()
#     data.iloc[0] = first_data

#     # 0.5 * interval => 0.5 * ((n_samples / sr) * 1000) / n_samples = 500 / sr
#     const = 500 / sr
#     data *= const
#     return data


# def vel_df(acc_df: pd.DataFrame):
#     dfs = []
#     for i in range(len(acc_df.columns) // 4096):
#         df = acc_df.iloc[:, i * 4096: (i + 1) * 4096]

#         df = df.apply(acc2vel, axis=1)

#         dfs += [df]
#     return pd.concat(dfs, axis=1)


# test_vel = vel_df(acc_df=burst_acc)
