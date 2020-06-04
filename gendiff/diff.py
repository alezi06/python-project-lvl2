import os
import json
import yaml


NESTED, UNCHANGED, CHANGED = 'nested', 'unchanged', 'changed'
REMOVED, ADDED = 'removed', 'added'


def parse(path_to_file):
    _, extension = os.path.splitext(path_to_file)
    if extension in {'.json', '.JSON', '.Json'}:
        return json.load(open(path_to_file))
    elif extension in {'.yml', '.YML', '.yaml'}:
        return yaml.safe_load(open(path_to_file))


def build_diff(before, after):
    keys_before = before.keys()
    keys_after = after.keys()
    result = {}

    for key in keys_before & keys_after:
        if isinstance(before[key], dict) and isinstance(after[key], dict):
            result[key] = (NESTED, build_diff(before[key], after[key]))
        elif before[key] == after[key]:
            result[key] = (UNCHANGED, after[key])
        else:
            result[key] = (CHANGED, (before[key], after[key]))

    result.update(
        {key : (REMOVED, before[key]) for key in keys_before - keys_after}
    )
    result.update(
        {key : (ADDED, after[key]) for key in keys_after - keys_before}
    )
    return result


def generate_diff(path_to_file1, path_to_file2, format):
    before = parse(path_to_file1)
    after = parse(path_to_file2)

    diff = build_diff(before, after)

    return format(diff)
