import unittest
from Finder import create_finder

class TestFinder(unittest.TestCase):
	
	def test_empty(self):
		finder = create_finder()
		self.assertEqual(finder.find('xyz'),[])
	
	def test_no_match(self):
		finder =create_finder(['abcd','dacb','lmn'])
		self.assertEqual(finder.find('xyz'),[])
	
	def test_match(self):
		finder = create_finder(['abcd','dacb','lmn'])
		self.assertEqual(finder.find('bcad'),['abcd','dacb'])	

if __name__ == '__main__':
	unittest.main()