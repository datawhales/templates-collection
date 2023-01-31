from typing import List, Any, Union
import random


# random.randint()
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


# random.randrange()
def sample_one_int_with_step(start: int, stop: int, step: int) -> int:
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


# random.sample()
def sample_k_items(x: List[Any], k: int, counts: Union[List[int], None] = None) -> List[Any]:
    """입력 받은 리스트에서 k개 item을 샘플링하여 리스트로 반환하는 함수.
    
    Args:
        x (List[Any]): 샘플링하고자 하는 원소가 들어 있는 리스트.
        k (int): 샘플링하고자 하는 개수.
        counts (Union[List[int], None]): 각 원소가 들어 있는 개수. Default 값(None)이면 하나씩 들어 있다고 간주.

    Returns:
        (List[Any]): 샘플링한 item들이 들어 있는 리스트.

    Examples:
        >>> x = [1, 2, 3, 4, 5, 6, 7]
        >>> result = sample_k_items(x=x, k=3, counts=[3, 4, 2, 2, 3, 1, 1])
        >>> print(result)
        [2, 1, 5]
    """
    SEED = 42
    random.seed(SEED)

    # 리스트에서 k개 item을 샘플링
    ret = random.sample(
        population=x,
        k=k,
        counts=counts,
    )
    return ret


# random.random()
def sample_one_float() -> float:
    """0 이상 1 미만의 임의의 소수를 샘플링하는 함수."""
    SEED = 42
    random.seed(SEED)

    # 0 <= float < 1을 만족하는 임의의 float를 샘플링
    ret = random.random()
    return ret


# random.uniform()
def sample_one_float_in_interval(low: float, high: float) -> float:
    """특정 구간 안에서 임의의 소수를 샘플링하는 함수."""
    SEED = 42
    random.seed(SEED)

    # low <= float <= high를 만족하는 임의의 float를 샘플링
    ret = random.uniform(
        a=low,
        b=high,
    )
    return ret


# random.gauss()
def sample_from_gaussian_distribution(mu: float = 0.0, sigma: float = 1.0) -> float:
    """가우시안 분포로부터 표본을 샘플링하는 함수."""
    SEED = 42
    random.seed(SEED)

    # 가우시안 분포로부터 1개 샘플링
    ret = random.gauss(
        mu=mu,
        sigma=sigma,
    )
    return ret
