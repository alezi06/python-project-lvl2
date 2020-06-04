import os
import json
import pytest
from gendiff import format
from gendiff.diff import generate_diff


def get_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(path_to_file):
    with open(path_to_file, 'r') as f:
        result = f.read()
    return result


def test_generate_diff():
    assert generate_diff(
        get_path('before.json'),
        get_path('after.json'),
        format.pretty
    ) == read(get_path('pretty'))

    assert generate_diff(
        get_path('before.yml'),
        get_path('after.yml'),
        format.pretty
    ) == read(get_path('pretty'))

    assert generate_diff(
        get_path('before.json'),
        get_path('after.json'),
        format.plain
    ) == read(get_path('plain'))

    assert generate_diff(
        get_path('before.yml'),
        get_path('after.yml'),
        format.plain
    ) == read(get_path('plain'))

    assert json.loads(generate_diff(
        get_path('before.json'),
        get_path('after.json'),
        format.json
    )) == json.loads(read(get_path('result.json')))

    assert json.loads(generate_diff(
        get_path('before.yml'),
        get_path('after.yml'),
        format.json
    )) == json.loads(read(get_path('result.json')))
