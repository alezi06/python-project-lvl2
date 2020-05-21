import json
import yaml


HANDLERS = {
    'json': json.load,
    'yml': yaml.safe_load,
}


def parse(file_content, type):
    return HANDLERS[type](file_content)
