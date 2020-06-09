import os
import json
import yaml


NESTED, UNCHANGED, CHANGED = 'nested', 'unchanged', 'changed'
REMOVED, ADDED = 'removed', 'added'


def parse(path_to_file):
    _, extension = os.path.splitext(path_to_file)
    extension = extension.lower()
    if extension == '.json':
        return json.load(open(path_to_file))
    elif extension in {'.yml', '.yaml'}:
        return yaml.safe_load(open(path_to_file))
    else:
        raise ValueError(f'Неверный формат файла: {extension}')


def build_diff(before, after):
    result = {}

    for key in before.keys() & after.keys():
        if isinstance(before[key], dict) and isinstance(after[key], dict):
            result[key] = (NESTED, build_diff(before[key], after[key]))
        elif before[key] == after[key]:
            result[key] = (UNCHANGED, after[key])
        else:
            result[key] = (CHANGED, (before[key], after[key]))

    def update_result_with(status, dict1, dict2):
        result.update(
            {key: (status, dict1[key]) for key in dict1.keys() - dict2.keys()}
        )

    update_result_with(REMOVED, before, after)
    update_result_with(ADDED, after, before)

    return result


def generate_diff(path_to_file1, path_to_file2, format):
    before = parse(path_to_file1)
    after = parse(path_to_file2)

    diff = build_diff(before, after)

    return format(diff)
