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
    expected = get_fixture('stylish_output')

    assert gendiff() == expected
