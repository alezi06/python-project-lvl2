import json


def deep_sort(items):
    items.sort(key=lambda x: x[1])
    for type_, _, value in items:
        if type_ == 'nested':
            deep_sort(value)


def render_to_json(diff):
    deep_sort(diff)
    return json.dumps(diff, indent=2)
