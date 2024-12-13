def get_indent(depth, size=2, space=' '):
    return space * (depth * size)

def get_stylish_value(value, depth):

    return f'{value}'

def get_formatted_value(value, depth):
    if isinstance(value, dict):
        return get_stylish_value(value, depth)
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return value

def stylish(diff):
    def inner(node, depth=0):
        node_type = node.get('type')
        key = node.get('key')

        match node_type:
            case 'added':
                value = node.get('value')
                formatted_value = get_formatted_value(value, depth)
                result = f'{get_indent(depth)}+ {key}: {formatted_value}'
                return result
            case 'removed':
                value = node.get('value')
                formatted_value = get_formatted_value(value, depth)
                result = f'{get_indent(depth)}- {key}: {formatted_value}'
                return result
            case 'unchanged':
                value = node.get('value')
                formatted_value = get_formatted_value(value, depth)
                result = f'{get_indent(depth)}  {key}: {formatted_value}'
                return result
            case 'nested':
                children = node.get('children')
                formatted_children = '\n'.join(list(map(lambda child: inner(child, depth + 1), children)))
                result = f'{get_indent(depth)}  {key}: {{{formatted_children}\n{get_indent(depth)}}}'
                return result
            case 'changed':
                old_value = node.get('old_value')
                formatted_old_value = get_formatted_value(old_value, depth)

                new_value = node.get('new_value')
                formatted_new_value = get_formatted_value(new_value, depth)

                result_before = f'{get_indent(depth)}- {key}: {formatted_old_value}'
                result_after = f'{get_indent(depth)}- {key}: {formatted_new_value}'
                return '\n'.join([result_before, result_after])
        raise ValueError(f'Unknown type: {node_type}')

    return '\n'.join(['{', *list(map(inner, diff)), '}'])
