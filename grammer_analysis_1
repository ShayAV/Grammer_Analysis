#!usr/bin/env python

#creator: Shay Avrahami

import en
import re
import inflect

class Grammer_Analysis_1(object):

	my_inflect = inflect.engine()

	def __init__(self, sentence):

		self.string = sentence

	def get_sentence(self):

		return self.string	

	# returns a list which describes a grammatical kind of each word in the sentence	
	def find_grammatical_kind(self):

		st = self.get_sentence()
		st = re.sub(',', "", st) # delete all commas
		result = []
		
		m = st.split(" ")
		
		for each in m:
			flag = False
			if en.noun.is_emotion(each):
				result.append("emotion")
				flag = True
			elif en.is_connective(each):
				result.append("connective")
				flag = True
			elif en.is_verb(each):
				result.append("verb")
				flag = True
			elif en.is_adjective(each):
				result.append("adjective")
				flag = True
			elif en.is_noun(each):
				result.append("noun")
				flag = True
			elif en.is_persuasive(each):
				result.append("persuasive")
				flag = True
			elif en.is_number(each):
				result.append("number")
				flag = True
			if flag == False:	
				result.append("unclear")					

		return result

	# calculates the percentage of the "emotion words" in the sentence	
	def emotions_percentage(self):

		st = self.get_sentence()
		m = st.split(" ")
		num_of_words = len(m) # amount of words in the sentence
		actual_emotions = 0 # amount of emotional words

		for each in m:
			if en.noun.is_emotion(each):
				actual_emotions += 1

		result = (actual_emotions * 100) / num_of_words
		result = str(result) + '%'
		return result

	# turns a sentence to plural form
	def singular_to_plural(self):

		final_list = []
		st = self.get_sentence()

		list_seperate_by_comma = st.split(",") # divide the sentence to list of strings by all the ','
		for each in list_seperate_by_comma:
	
			if each[0] == ' ': # prevent bug
				each = each[1:]
			m = each.split(" ") # split each sentence to list of words

			plural_list = []
		
			for each in m:
				if en.is_noun(each):
					each = en.noun.plural(each)
				elif en.is_adjective(each):
					each = en.adjective.plural(each)
				elif en.is_connective(each):
					each = self.my_inflect.plural(each)
				elif en.is_persuasive(each):
					each = en.persuasive.plural(each)
				plural_list.append(each)

			plural_list = ' '.join(plural_list) # convert each list to string
			final_list.append(plural_list)
		
		final_list = ', '.join(final_list)	
		return final_list

		#tokens = nltk.word_tokenize(st)
		#print tokens	

if __name__ == "__main__":

	c = Grammer_Analysis_1("I love this apple, it is very tasty")

	print c.find_grammatical_kind()
	print c.emotions_percentage()
	print c.singular_to_plural()

	
