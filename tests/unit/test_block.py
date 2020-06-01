import unittest
from unittest.mock import Mock, patch


def mock_repr():
    return 'Block - 123'


class TestBlock(unittest.TestCase):
    @patch('block.Block.__repr__', side_effect=mock_repr)
    def test_block_output(self, __repr__):
        self.assertEqual(__repr__(), 'Block - 123')


