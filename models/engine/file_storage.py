#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes JSON file
to instances"""
import json
import os


class FileStorage:
    __file_path = "file.json"
    __object = {}
