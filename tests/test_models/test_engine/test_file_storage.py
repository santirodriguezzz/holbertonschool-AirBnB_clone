#!/usr/bin/python3
"""testing"""
import unittest
from models import storage
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class File_Storage_Tests(unittest.TestCase):
    """tests file storage file"""

    def test__FilePath(self):
        """tests attr file_path"""

    def test_filestorage(self):
        storage = FileStorage()
        storage.all().clear()
        storage.reload()
        self.assertFalse(len(storage.all()) == 0)

if __name__ == "__main__":
    unittest.main()
