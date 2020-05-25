def to_str(value):
    if isinstance(value, dict):
        return "'complex value'"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value


def get_full_path(acc, key):
    return '.'.join([*acc, key])


def render(items, acc):
    items.sort(key=lambda x: x[1])
    mapping = {
        'nested': lambda k, v: (
            render(v, [*acc, k])
        ),
        'changed': lambda k, v: (
            f"Property '{get_full_path(acc, k)}' was changed. " +
            f"From {to_str(v[0])} to {to_str(v[1])}"
        ),
        'removed': lambda k, v: (
            f"Property '{get_full_path(acc, k)}' was removed"
        ),
        'added': lambda k, v: (
           f"Property '{get_full_path(acc, k)}' " +
           f"was added with value: {to_str(v)}"
        ),
    }
    filtered = filter(lambda x: x[0] != 'unchanged', items)

    return '\n'.join(
        [mapping[type_](key, value) for type_, key, value in filtered]
    )


def render_to_plain(diff):
    return render(diff, [])
