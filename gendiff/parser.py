import json


def parser(content, format):
    match format:
        case 'json':
            return json.loads(content)# json
        case 'yaml' | 'yml':
            return # yml
    raise ValueError(f'Unknown format: #{format}')
