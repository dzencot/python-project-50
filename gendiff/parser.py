import json

import yaml


def parser(content, format):
    match format:
        case 'json':
            return json.loads(content)  # json
        case 'yaml' | 'yml':
            return yaml.load(content, Loader=yaml.FullLoader)  # yml
    raise ValueError(f'Unknown format: {format}')
