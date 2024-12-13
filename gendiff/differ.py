

def get_diff(first_data, second_data):
    union_keys = sorted(first_data.keys() | second_data.keys())

    def comparator(key):
        first_value = first_data.get(key)
        second_value = second_data.get(key)
        if key not in first_data:
            return {
                'key': key,
                'type': 'added',
                'value': second_value
            }
        if key not in second_data:
            return {
                'key': key,
                'type': 'removed',
                'value': first_value
            }
        if first_value == second_value:
            return {
                'key': key,
                'type': 'unchanged',
                'value': first_value
            }
        if isinstance(first_value, dict) and isinstance(second_value, dict):
            return {
                'key': key,
                'type': 'nested',
                'children': get_diff(first_value, second_value)
            }
        return {
            'key': key,
            'type': 'changed',
            'old_value': first_value,
            'new_value': second_value
        }
    
    result = list(map(comparator, union_keys))

    return result
