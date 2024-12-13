from pathlib import Path

from gendiff.differ import get_diff
from gendiff.formatter import format
from gendiff.parser import parser


def get_absolute_path(path):
    return Path.joinpath(Path.cwd(), path)


def get_content(filename):
    return get_absolute_path(filename).read_text()


def get_data_format(path):
    file_extension = Path(path).suffix
    return file_extension[1:]


def generate_diff(first_file_path, second_file_path, format_name='stylish'):
    first_content = get_content(first_file_path)
    first_content_format = get_data_format(first_file_path)

    second_content = get_content(second_file_path)
    second_content_format = get_data_format(second_file_path)

    first_parsed = parser(first_content, first_content_format)
    second_parsed = parser(second_content, second_content_format)

    diff = get_diff(first_parsed, second_parsed)
    
    formatted = format(diff, format_name)

    return formatted
