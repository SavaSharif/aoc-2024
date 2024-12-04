import pytest
# from common.utils import read_file
# from common.utils import read_file
from day_01 import p1

def read_file(file_path):
    with open(file_path, 'r') as f:
        return [x.strip() for x in f.readlines()]

@pytest.mark.parametrize(
    "filename, expected",
    [
        pytest.param(
            "01/test_input.txt", 11, id="test_input.txt",
        ),
    ],
)
def test_p1(filename, expected):
    # Test cases for p1 function
    result = p1(read_file(filename))
    print(result)
    assert result == expected


# @pytest.mark.parametrize(
#     "filename, expected",
#     [
#         pytest.param(
#             "01/test_input_2.txt", 281, id="test - 1",
#         ),
#     ],
# )
# def test_p2(filename, expected):
#     # Test cases for p2 function
#     assert p2(read_file(filename)) == expected
