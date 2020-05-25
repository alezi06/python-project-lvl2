from gendiff.formatters.pretty import render_to_pretty
from gendiff.formatters.plain import render_to_plain


HANDLERS = {
    'pretty': render_to_pretty,
    'plain': render_to_plain,
}


def render_to_format(diff, format_):
    return HANDLERS[format_](diff)
