#!/usr/bin/python3
# 6-from_json_string.py
# ikeji chiagozie @ alx-school
"""Defines a JSON-to-object function."""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string."""
    return json.loads(my_str)
