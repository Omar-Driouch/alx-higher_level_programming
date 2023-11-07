#!/usr/bin/python3
import json
"""Module for converting an object to a JSON string."""


def to_json_string(my_obj):
    """Converts an object to a JSON string.

    Args:
        my_obj: The object to convert.

    Returns:
        The JSON string representation of the object.
    """
    return json.dumps(my_obj)
