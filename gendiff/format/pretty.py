from gendiff import diff


def indent(depth):
    return '  ' * depth


def to_str(value, depth):
    if not isinstance(value, dict):
        return value
    result = '\n'.join([f'{k}: {v}' for k, v in value.items()])
    return f'{{\n{indent(depth + 3)}{result}\n{indent(depth + 1)}}}'


def render(diff_data, depth=1):
    lines = []
    for key, (status, value) in sorted(diff_data.items()):
        def store(symbol, value):
            lines.append(
                f'{indent(depth)}{symbol} {key}: {to_str(value, depth)}'
            )

        if status == diff.NESTED:
            lines.append(
                f'{indent(depth)}  {key}: '
                f'{{\n{render(value, depth + 2)}\n{indent(depth + 1)}}}'
            )
        elif status == diff.UNCHANGED:
            store(' ', value)
        elif status == diff.CHANGED:
            old, new = value
            store('+', new)
            store('-', old)
        elif status == diff.REMOVED:
            store('-', value)
        elif status == diff.ADDED:
            store('+', value)

    return '\n'.join(lines)


def format(diff):
    return f'{{\n{render(diff)}\n}}'
