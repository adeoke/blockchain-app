import unittest
from unittest.mock import Mock, patch


class TestBlockchain(unittest.TestCase):
    @patch('blockchain.Blockchain.__repr__',
           return_value='Blockchain - [Block - one, Block - two]')
    def test_add_block(self, __repr__):
        self.assertEqual(__repr__(), 'Blockchain - [Block - one, Block - two]')
