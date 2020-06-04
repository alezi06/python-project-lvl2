from gendiff import diff


def to_str(value):
    if isinstance(value, dict):
        return "'complex value'"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return value


def get_full_path(acc, key):
    return '.'.join([*acc, key])


def render(diff_data, acc):
    lines = []
    for key, (status, value) in sorted(diff_data.items()):
        if status == diff.NESTED:
            lines.append(render(value, [*acc, key]))
        elif status == diff.CHANGED:
            old, new = value
            lines.append(
                f"Property '{get_full_path(acc, key)}' was changed. " +
                f"From {to_str(old)} to {to_str(new)}"
            )
        elif status == diff.REMOVED:
            lines.append(
                f"Property '{get_full_path(acc, key)}' was removed"
            )
        elif status == diff.ADDED:
            lines.append(
                f"Property '{get_full_path(acc, key)}' " +
                f"was added with value: {to_str(value)}"
            )

    return '\n'.join(lines)


def format(diff):
    return render(diff, [])
