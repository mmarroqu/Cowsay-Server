import os
import random

class Cow():

	def __init__(self, inputFile):
		quoteFile = open(inputFile)
		self.quotes = list()
		self.numQuotes = 0
		for line in quoteFile:
			self.quotes.append(line.rstrip())
			self.numQuotes+=1

	def getRandomQuote(self):
		return self.quotes[random.randint(0, self.numQuotes-1)]

	def speak(self):
		return(os.popen("cowsay " +"'"+self.getRandomQuote()+ "'").read())
		



