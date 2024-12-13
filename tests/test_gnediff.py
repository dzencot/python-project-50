
from pathlib import Path

import pytest

from gendiff.gendiff import gendiff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def get_test_data(filename):
    return get_test_data_path(filename).read_text()


stylish_expected = get_test_data('stylish_output').strip()
plain_expected = get_test_data('plain_output').strip()
json_expected = get_test_data('json_output').strip()

file_formats = ['json', 'yml']


@pytest.mark.parametrize("file_format", file_formats)
def test_gendiff(file_format):
    first_file_path = get_test_data_path(f'file1.{file_format}')
    second_file_path = get_test_data_path(f'file2.{file_format}')

    assert gendiff(first_file_path, second_file_path, 'stylish') == stylish_expected  # noqa: E501
    assert gendiff(first_file_path, second_file_path, 'plain') == plain_expected
    assert gendiff(first_file_path, second_file_path, 'json') == json_expected
