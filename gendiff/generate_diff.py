import os
from gendiff.parser import parse


def to_str(key, value, flag=' '):
    return f'  {flag} {key}: {value}'


def generate_diff(path_to_file1, path_to_file2):
    _, extension1 = os.path.splitext(path_to_file1)
    _, extension2 = os.path.splitext(path_to_file2)

    before = parse(open(path_to_file1), extension1[1:])
    after = parse(open(path_to_file2), extension2[1:])

    before_keys = set(before)
    after_keys = set(after)

    result = []
    for key in before_keys & after_keys:
        if before[key] == after[key]:
            result.append(to_str(key, after[key]))
        else:
            result.append(to_str(key, after[key], '+'))
            result.append(to_str(key, before[key], '-'))

    result.extend(
        [to_str(key, before[key], '-') for key in before_keys - after_keys]
    )
    result.extend(
        [to_str(key, after[key], '+') for key in after_keys - before_keys]
    )

    return '{\n' + '\n'.join(result) + '\n}'
