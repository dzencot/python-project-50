import os

from gendiff.differ import get_diff
from gendiff.formatter.main import format
from gendiff.parser import parser


def get_absolute_path(path):
    return os.path.join(os.getcwd(), path)


def get_content(path):
    absolute_path = get_absolute_path(path)
    fd = open(absolute_path) 
    data = fd.read()
    fd.close()
    return data


def get_data_format(path):
    _, file_extension = os.path.splitext(path)
    return file_extension[1:]


def gendiff(first_file_path, second_file_path, format_name='stylish'):
    first_content = get_content(first_file_path)
    first_content_format = get_data_format(first_file_path)

    second_content = get_content(second_file_path)
    second_content_format = get_data_format(second_file_path)

    first_parsed = parser(first_content, first_content_format)
    second_parsed = parser(second_content, second_content_format)

    diff = get_diff(first_parsed, second_parsed)
    
    formatted = format(diff, format_name)

    return formatted
