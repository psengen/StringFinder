class Finder:
	def __init__(self,words):
		self.words = words

	def find(self,word):
		res = [i for i in self.words if sorted(word)==sorted(i)] 
		return res

def create_finder(word_list=[]):
	finder = Finder(word_list)
	return finder