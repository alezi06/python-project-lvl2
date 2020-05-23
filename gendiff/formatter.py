def indent(depth):
    return '  ' * depth


def to_str(value, depth):
    if not isinstance(value, dict):
        return value
    result = '\n'.join([f'{k}: {v}' for k, v in value.items()])
    return '{\n' + f'{indent(depth + 3)}{result}\n{indent(depth + 1)}' + '}'


def render(items, depth=1):
    items.sort(key=lambda x: x[1])
    mapping = {
        'nested': lambda k, v: (
            f'{indent(depth)}  {k}: ' + '{\n' +
            f'{render(v, depth + 2)}\n{indent(depth + 1)}' + '}'
        ),
        'unchanged': lambda k, v: (
            f'{indent(depth)}  {k}: {to_str(v, depth)}'
        ),
        'changed': lambda k, v: (
            f'{indent(depth)}+ {k}: {to_str(v[1], depth)}\n' +
            f'{indent(depth)}- {k}: {to_str(v[0], depth)}'
        ),
        'removed': lambda k, v: (
            f'{indent(depth)}- {k}: {to_str(v, depth)}'
        ),
        'added': lambda k, v: (
            f'{indent(depth)}+ {k}: {to_str(v, depth)}'
        ),
    }

    return '\n'.join(
        [mapping[type_](key, value) for type_, key, value in items]
    )


def render_to_format(diff):
    return '{\n' + render(diff) + '\n}'
