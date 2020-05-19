import json


def to_str(key, value, flag=' '):
    return f'  {flag} {key}: {value}'


def generate_diff(path_to_file1, path_to_file2):
    before = json.load(open(path_to_file1))
    after = json.load(open(path_to_file2))

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
