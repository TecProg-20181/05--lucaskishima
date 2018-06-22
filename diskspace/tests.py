import unittest
from diskspace import *

class TestDiskSpace(unittest.TestCase):

    def setUp(self):
        #used in test_bytes_to_readable
        self.blocks = 8
        self.bytesOfBlocks = '4.00Kb'

    def test_bytes_to_readable(self):
        command = bytes_to_readable(self.blocks)
        self.assertEqual(command, self.bytesOfBlocks)


if __name__ == '__main__':
    unittest.main()
