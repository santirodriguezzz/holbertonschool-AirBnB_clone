#!/usr/bin/python3
"""testing"""
import unittest
from models.engine.file_storage import FileStorage


class File_Storage_Tests(unittest.TestCase):
    """tests file storage file"""

    def test0(self):
        """tests file storage methods"""
        file1 = FileStorage()

        self.assertEqual(file1.all(), {})

if __name__ == '__main__':
    unittest.main()
