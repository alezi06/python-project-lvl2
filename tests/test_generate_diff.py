import os
import pytest
from gendiff.generate_diff import generate_diff


def get_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(path_to_file):
    with open(path_to_file, 'r') as f:
        result = f.read()
    return result


@pytest.mark.parametrize(
    ('before', 'after', 'output', 'expected'), [
        (
            get_path('before.json'), get_path('after.json'),
            'pretty', read(get_path('pretty'))
        ),
        (
            get_path('before.yml'), get_path('after.yml'),
            'pretty', read(get_path('pretty'))
        ),
        (
            get_path('before.json'), get_path('after.json'),
            'plain', read(get_path('plain'))
        ),
        (
            get_path('before.yml'), get_path('after.yml'),
            'plain', read(get_path('plain'))
        ),
        (
            get_path('before.json'), get_path('after.json'),
            'json', read(get_path('json'))
        ),
        (
            get_path('before.yml'), get_path('after.yml'),
            'json', read(get_path('json'))
        ),

    ]
)
def test_generate_diff(before, after, output, expected):
    assert generate_diff(before, after, output) == expected
