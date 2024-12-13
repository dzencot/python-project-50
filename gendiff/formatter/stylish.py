def get_indent(depth, size=4, space=' '):
    return space * ((depth * size) - 2)


def get_stylish_value(value, depth):
    prepared = list(map(lambda key:
        f'{get_indent(depth)}  {key}: {get_formatted_value(value.get(key),
        depth)}', value))
    formatted = '\n'.join(prepared)
    return f'{{\n{formatted}\n  {get_indent(depth - 1)}}}'


def get_formatted_value(value, depth):
    if isinstance(value, dict):
        return get_stylish_value(value, depth + 1)
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value is None:
        return 'null'
    return value


def stylish(diff):
    def inner(node, depth=1):
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
                formatted_children = '\n'.join(list(map(
                    lambda child: inner(child, depth + 1), children)))
                result = f'{get_indent(depth)}  {key}: {{\n{formatted_children}\n  {get_indent(depth)}}}'  # noqa: E501
                return result
            case 'changed':
                old_value = node.get('old_value')
                formatted_old_value = get_formatted_value(old_value, depth)

                new_value = node.get('new_value')
                formatted_new_value = get_formatted_value(new_value, depth)

                result_before = f'{get_indent(depth)}- {key}: {formatted_old_value}'  # noqa: E501
                result_after = f'{get_indent(depth)}+ {key}: {formatted_new_value}'  # noqa: E501
                return '\n'.join([result_before, result_after])
        raise ValueError(f'Unknown type: {node_type}')

    return '\n'.join(['{', *list(map(inner, diff)), '}'])
