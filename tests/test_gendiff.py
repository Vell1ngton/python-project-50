from project50 import generate_diff
import pytest

@pytest.mark.parametrize('file1, file2, expected',
                         [
                             ('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'tests/fixtures/result1.txt')
                         ])
def test_generate_diff(file1, file2, expected):
    with open(expected) as file:
        result = file.read()
        assert generate_diff(file1,file2) == result