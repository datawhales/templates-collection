import pandas as pd
import numpy as np


class ConvertEpochTime:
    """Epoch time을 datetime으로 변환."""
    @staticmethod
    def example():
        """1. scalar epoch time을 datetime으로 변환."""
        from datetime import datetime

        epoch_t = 1645565480

        # Local 시간으로 변경
        datetime_obj = datetime.fromtimestamp(epoch_t)
        datetime_str = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
        print(datetime_str)

        # UTC 시간으로 변경
        utc_datetime_obj = datetime.utcfromtimestamp(epoch_t)
        utc_datetime_str = utc_datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
        print(utc_datetime_str)


    @staticmethod
    def example_2():
        """2. 데이터프레임 내의 epoch time column을 datetime으로 변환."""
        import pandas as pd

        df = pd.DataFrame({"epoch_time": [1645565480, 1645565580, 1645565680]})

        # UTC 시간으로 변경
        df["datetime"] = pd.to_datetime(df["epoch_time"], unit="s")


if __name__ == "__main__":
    ConvertEpochTime.example()
    ConvertEpochTime.example_2()
