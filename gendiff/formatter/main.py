import json
from gendiff.formatter.plain import plain
from gendiff.formatter.stylish import stylish



def format(tree, format_name):
    match format_name:
        case 'stylish':
            return stylish(tree)
        case 'plain':
            return plain(tree)
        case 'json':
            return json.dumps(tree)
    raise ValueError(f'Unknown format name: {format_name}')
