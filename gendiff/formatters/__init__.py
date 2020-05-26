from gendiff.formatters.pretty import render_to_pretty
from gendiff.formatters.plain import render_to_plain
from gendiff.formatters.json import render_to_json


HANDLERS = {
    'pretty': render_to_pretty,
    'plain': render_to_plain,
    'json': render_to_json,
}


def render_to_format(diff, format_):
    return HANDLERS[format_](diff)
