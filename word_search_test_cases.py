import unittest
from unittest.mock import MagicMock

from word_search import WordSearcher

class WordSearchTest(unittest.TestCase):
	def test_file_does_not_exist(self):
		# test that non-existent files are handled
		ws = WordSearcher()
		self.assertRaises(IOError, ws.read_in_file, "fake_path")

	def test_file_parsed(self):
		ws = WordSearcher()
		test_data = ["Book", "Cobb", "Frye", "Reynolds", "Serra", "Tam", "Washburne"]
		words, graph = ws.read_in_file("./test_case_one.txt")
		assert words == test_data

if __name__ == "__main__":
	unittest.main()