#!/usr/bin/python3
"""Python interpreter"""
from msilib.schema import File
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
