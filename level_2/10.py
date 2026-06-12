from constants import ___
from collections.abc import Sequence

Point = tuple[int, int] 

def is_point_in_square(point: Sequence[Point], left_upper_corner: Sequence[Point], right_bottom_corner: Sequence[Point]) -> bool:
    pass


if __name__ == "__main__":
    assert is_point_in_square(
        point=(10, 12),
        left_upper_corner=(5, 5),
        right_bottom_corner=(20, 15)
    ) is True
