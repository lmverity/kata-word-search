import csv
import os
import re
import unittest

from word_search import WordSearcher

TEST_FILES = {}

class WordSearchTest(unittest.TestCase):
	def setUp(self):
		# walk test directory to get all test files and parse each
		test_files = os.walk("./test_files")
		for _, _, files in test_files:
			for file in files:
				words = []
				grid = []
				absolute_path = os.path.abspath("./test_files/" + file)
				with open(absolute_path, "r") as f:
					reader = csv.reader(f)
					words = next(reader)
					points = next(reader)
					for row in reader:
						grid.append(row)
			test_name = re.search("test_(.*).txt", file)[1]
			point_list = []
			for point in range(0, len(points), 2):
				point_list.append((points[point], points[point+1]))
			TEST_FILES[test_name] = (words, grid, point_list)

	def test_file_does_not_exist(self):
		# test that non-existent files are handled
		ws = WordSearcher()
		self.assertRaises(IOError, ws.read_in_file, "fake_path")

	def test_file_return_value(self):
		# test that csv file parsed and properly returned
		ws = WordSearcher()
		test_data = ["Book", "Cobb", "Frye", "Reynolds", "Serra", "Tam", "Washburne"]
		words, graph = ws.read_in_file("./test_files/test_csv_parsed.txt")
		assert words == test_data

	def test_horizontal(self):
		# test that a horizontal word is detected
		ws = WordSearcher()
		words, grid, points = TEST_FILES["horizontal"]
		found_word_location = ws.search_for_words(words, grid)
		assert found_word_location == points

if __name__ == "__main__":
	unittest.main()