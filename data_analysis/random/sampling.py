from typing import List, Any
import random


def sample_one_int(low: int, high: int) -> int:
    """두 정수 사이의 임의의 정수 하나를 샘플링하는 함수."""
    SEED = 42
    random.seed(SEED)

    # low <= N <= high 를 만족하는 임의의 정수 N을 샘플링
    ret = random.randint(
        a=low,
        b=high,
    )
    return ret


def sample_one_int_with_step(start: int, stop: int, step: int):
    """두 정수 중 작은 정수부터 일정한 간격을 가지며 증가하는 수열에서 임의의 정수 하나를 샘플링하는 함수."""
    SEED = 42
    random.seed(SEED)

    # start부터 시작하여 일정한 간격 step으로 증가하는 수열에서 임의의 정수 N을 샘플링
    ret = random.randrange(
        start=start,
        stop=stop,
        step=step,
    )
    return ret


def shuffle_list(x: List[Any]) -> List:
    """입력 받은 리스트를 셔플한 뒤 반환하는 함수."""
    SEED = 42
    random.seed(SEED)

    # 리스트 x를 셔플
    random.shuffle(x=x)
    return x

# https://docs.python.org/ko/3.9/library/random.html
# random.sample
# random.choice
# random.random
# random.uniform
# random.gauss

if __name__ == "__main__":
    x = [1,2,3,4,5,6,7,8,9,10]
    print(shuffle_list(x))
