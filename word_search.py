import csv
import os

class WordSearcher():
	def read_in_file(self, path_name):
		words = []
		grid = []
		try:
			with open(path_name, "r") as f:
				reader = csv.reader(f)
				words = next(reader)
				for row in reader:
					grid.append(row)
		except IOError:
			print("File does not exist!")
			raise IOError

		return words, grid
