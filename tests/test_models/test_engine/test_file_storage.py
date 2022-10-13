#!/usr/bin/python3
"""testing"""
import unittest
from models.engine.file_storage import FileStorage
from models import storage


class File_Storage_Tests(unittest.TestCase):
    """tests file storage file"""

    def test0(self):
        """tests file storage methods"""
        file1 = FileStorage()
        file1_list = storage.all()
        self.assertEqual(type(file1_list), dict)

if __name__ == '__main__':
    unittest.main()
