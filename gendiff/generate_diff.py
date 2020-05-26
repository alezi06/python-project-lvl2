import os
from gendiff.parser import parse
from gendiff.formatters import render_to_format


def build_diff(before, after):
    result = []
    before_keys = set(before)
    after_keys = set(after)

    for key in before_keys & after_keys:
        if isinstance(before[key], dict) and isinstance(after[key], dict):
            result.append(('nested', key, build_diff(before[key], after[key])))
        elif before[key] == after[key]:
            result.append(('unchanged', key, after[key]))
        else:
            result.append(('changed', key, (before[key], after[key])))

    result.extend(
        [('removed', key, before[key]) for key in before_keys - after_keys]
    )
    result.extend(
        [('added', key, after[key]) for key in after_keys - before_keys]
    )
    return result


def generate_diff(path_to_file1, path_to_file2, output):
    _, extension1 = os.path.splitext(path_to_file1)
    _, extension2 = os.path.splitext(path_to_file2)

    before = parse(open(path_to_file1), extension1[1:])
    after = parse(open(path_to_file2), extension2[1:])

    diff = build_diff(before, after)

    return render_to_format(diff, output)
