from typing import List, Any
import random


# random.shuffle()
def shuffle_list(x: List[Any]) -> List[Any]:
    """입력 받은 리스트를 셔플한 뒤 반환하는 함수."""
    SEED = 42
    random.seed(SEED)

    # 리스트 x를 셔플
    random.shuffle(x=x)
    return x


def example():
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    shuffled_x = shuffle_list(x=x)
    print(shuffled_x)


if __name__ == "__main__":
    example()
