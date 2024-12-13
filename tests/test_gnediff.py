import os

import pytest

from gendiff.gendiff import gendiff


def get_fixture_path(name):
    return os.path.join(os.path.dirname(__file__), 'fixtures', name)


def get_fixture(name):
    path = get_fixture_path(name)
    fd = open(path) 
    data = fd.read()
    fd.close()
    return data


stylish_expected = get_fixture('stylish_output').strip()
plain_expected = get_fixture('plain_output').strip()
json_expected = get_fixture('json_output').strip()

file_formats = ['json', 'yml']


@pytest.mark.parametrize("file_format", file_formats)
def test_gendiff(file_format):
    first_file_path = get_fixture_path(f'file1.{file_format}')
    second_file_path = get_fixture_path(f'file2.{file_format}')

    assert gendiff(first_file_path, second_file_path, 'stylish') == stylish_expected  # noqa: E501
    assert gendiff(first_file_path, second_file_path, 'plain') == plain_expected
    assert gendiff(first_file_path, second_file_path, 'json') == json_expected
