import pytest
from src import process_grades, longest_increasing_streak


@pytest.mark.parametrize(
    "test_data, expected",
    [
        pytest.param(
            [
                "Иванов: 85",
                "Петров: 42",
                "Сидоров: abc",
                "Козлов: 90",
                ": 55",
                "Иванов: 70",
            ],
            {
                "valid_count": 4,
                "average": 71.8,
                "passed": ["Иванов", "Козлов"],
                "skipped": 2,
            },
            id="hh example",
        )
    ],
)
@pytest.mark.unit
def test_process_grades(test_data, expected):
    assert process_grades(test_data) == expected


@pytest.mark.parametrize(
    "test_data, expected",
    [
        pytest.param(
            [1, 3, 2, 5, 8, 4, 7],
            {"length": 3, "streak": [2, 5, 8]},
            id="hh example",
        ),
        pytest.param(
            [1, 2, 3, 4, 5, 4, 7],
            {"length": 5, "streak": [1, 2, 3, 4, 5]},
            id="from the beginning",
        ),
        pytest.param(
            [1, 2, 1, 2, 3, 4, 5],
            {"length": 5, "streak": [1, 2, 3, 4, 5]},
            id="from the end",
        ),
        pytest.param(
            [1, 1, 1], {"length": 0, "streak": []}, id="single elements"
        ),
        pytest.param([], {"length": 0, "streak": []}, id="empty"),
        pytest.param([1], {"length": 0, "streak": []}, id="one element"),
        pytest.param(
            [1, 2, 3, 1, 8, 10, 7, 9],
            {"length": 3, "streak": [1, 2, 3]},
            id="double len",
        ),
    ],
)
@pytest.mark.unit
def test_longest_increasing_streak(test_data, expected):
    assert longest_increasing_streak(test_data) == expected
