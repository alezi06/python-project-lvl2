import os
from gendiff.parser import parse
from gendiff.formatter import render_to_format


def build_diff(before, after):
    diff = []
    before_keys = set(before)
    after_keys = set(after)

    for key in before_keys & after_keys:
        if isinstance(before[key], dict) and isinstance(after[key], dict):
            diff.append(('nested', key, build_diff(before[key], after[key])))
        elif before[key] == after[key]:
            diff.append(('unchanged', key, after[key]))
        else:
            diff.append(('changed', key, (before[key], after[key])))

    for key in before_keys - after_keys:
        diff.append(('removed', key, before[key]))

    for key in after_keys - before_keys:
        diff.append(('added', key, after[key]))

    return diff


def generate_diff(path_to_file1, path_to_file2):
    _, extension1 = os.path.splitext(path_to_file1)
    _, extension2 = os.path.splitext(path_to_file2)

    before = parse(open(path_to_file1), extension1[1:])
    after = parse(open(path_to_file2), extension2[1:])

    diff = build_diff(before, after)

    return render_to_format(diff)
