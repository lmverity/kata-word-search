import unittest
from unittest.mock import MagicMock

from word_search import WordSearcher

class WordSearchTest(unittest.TestCase):

	def test_file_exists(self):
		# test that non-existent files are handled
		ws = WordSearcher()
		self.assertRaises(IOError, ws.read_in_file, "fake_path")

if __name__ == "__main__":
	unittest.main()