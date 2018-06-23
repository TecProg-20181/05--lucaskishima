import unittest
import io
from diskspace import *
from unittest.mock import MagicMock

class TestDiskSpace(unittest.TestCase):

    def setUp(self):
        #used in test_bytes_to_readable
        self.blocks = 8
        self.bytesOfBlocks = "4.00Kb"

        #used in test_bytes_to_readable
        self.command = "du"
        self.result = subprocess.check_output(self.command.strip().split(' '))

        #used in test_print_tree
        self.file_tree = {'/home/lucas/unb/tecprog/05--lucaskishima/diskspace': {'print_size': '12.00Kb', 'children': [], 'size': 24}}
        self.file_tree_node = {'print_size': '12.00Kb', 'children': [], 'size': 24}
        self.path = '/home/lucas/unb/tecprog/05--lucaskishima/diskspace'
        self.largest_size = 7
        self.total_size = 24
        self.depth=0
        self.expected_output = '12.00Kb  100%  /home/lucas/unb/tecprog/05--lucaskishima/diskspace\n'

    def test_bytes_to_readable(self):
        command = bytes_to_readable(self.blocks)
        self.assertEqual(command, self.bytesOfBlocks)

    def test_subprocess_check_output(self):
        command = subprocess_check_output(self.command)
        self.assertEqual(command, self.result)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_tree(self, mock_stdout):
        print_tree(self.file_tree, self.file_tree_node, self.path, self.largest_size, self.total_size,
                   self.depth)
        self.assertEqual(mock_stdout.getvalue(), self.expected_output)

if __name__ == '__main__':
    unittest.main()
