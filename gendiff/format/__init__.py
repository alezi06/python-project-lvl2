from gendiff.format.pretty import format as pretty
from gendiff.format.plain import format as plain
from gendiff.format.json import format as json


FORMATTERS = (JSON, PLAIN, PRETTY) = (
    'json', 'plain', 'pretty'
)

__all__ = ('json', 'plain', 'pretty')
