import unittest
from diskspace import *

class TestDiskSpace(unittest.TestCase):

    def setUp(self):
        #used in test_bytes_to_readable
        self.blocks = 8
        self.bytesOfBlocks = '4.00Kb'

        #used in test_bytes_to_readable
        self.command = "du"
        self.result = subprocess.check_output(self.command.strip().split(' '))

    def test_bytes_to_readable(self):
        command = bytes_to_readable(self.blocks)
        self.assertEqual(command, self.bytesOfBlocks)

    def test_subprocess_check_output(self):
        command = subprocess_check_output(self.command)
        self.assertEqual(command, self.result)

if __name__ == '__main__':
    unittest.main()
