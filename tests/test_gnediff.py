import os
from gendiff.gendiff import gendiff


def get_fixture_path(name):
    return os.path.join(os.path.dirname(__file__), 'fixtures', name)

def get_fixture(name):
    path = get_fixture_path(name)
    fd = open(path) 
    data = fd.read()
    fd.close()
    return data

def test_json():
    expected = get_fixture('stylish_output').strip()
    first_file_path = get_fixture_path('file1.json')
    second_file_path = get_fixture_path('file2.json')

    assert gendiff(first_file_path, second_file_path, 'stylish') == expected
