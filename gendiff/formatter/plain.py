def get_formatted_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, bool):
        return 'true' if value else 'false'
    if value == None:
        return 'null'
    return f"'{value}'"

def plain(diff):
    def inner(node, paths=[]):
        node_type = node.get('type')
        key = node.get('key')
        new_paths = [*paths, key]

        match node_type:
            case 'added':
                value = node.get('value')
                property_name = '.'.join(new_paths)
                formatted_value = get_formatted_value(value)

                result = f"Property '{property_name}' was added with value: {formatted_value}"
                return result
            case 'removed':
                value = node.get('value')
                property_name = '.'.join(new_paths)

                result = f"Property '{property_name}' was removed"
                return result
            case 'unchanged':
                return None
            case 'nested':
                children = node.get('children')
                prepared = map(lambda child: inner(child, new_paths), children)
                filtered = filter(lambda item: item != None, prepared)
                return '\n'.join(list(filtered))
            case 'changed':
                property_name = '.'.join(new_paths)

                old_value = node.get('old_value')
                formatted_old_value = get_formatted_value(old_value)

                new_value = node.get('new_value')
                formatted_new_value = get_formatted_value(new_value)

                return f"Property '{property_name}' was updated. From {formatted_old_value} to {formatted_new_value}"
        raise ValueError(f'Unknown type: {node_type}')

    prepared = map(inner, diff)
    filtered = filter(lambda item: item != None, prepared)
    return '\n'.join(list(filtered))

