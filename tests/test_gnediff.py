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
    stylish_expected = get_fixture('stylish_output').strip()
    plain_expected = get_fixture('plain_output').strip()
    json_expected = get_fixture('json_output').strip()

    first_file_path = get_fixture_path('file1.json')
    second_file_path = get_fixture_path('file2.json')

    assert gendiff(first_file_path, second_file_path, 'stylish') == stylish_expected
    assert gendiff(first_file_path, second_file_path, 'plain') == plain_expected
    assert gendiff(first_file_path, second_file_path, 'json') == json_expected

def test_yaml():
    stylish_expected = get_fixture('stylish_output').strip()
    plain_expected = get_fixture('plain_output').strip()
    json_expected = get_fixture('json_output').strip()

    first_file_path = get_fixture_path('file1.yaml')
    second_file_path = get_fixture_path('file2.yml')

    assert gendiff(first_file_path, second_file_path, 'stylish') == stylish_expected
    assert gendiff(first_file_path, second_file_path, 'plain') == plain_expected
    assert gendiff(first_file_path, second_file_path, 'json') == json_expected

# def test_json():
#     expected = get_fixture('stylish_output').strip()
#     first_file_path = get_fixture_path('file1.json')
#     second_file_path = get_fixture_path('file2.json')

#     assert gendiff(first_file_path, second_file_path, 'stylish') == expected
