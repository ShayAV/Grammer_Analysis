#!usr/bin/env python

#creator: Shay Avrahami

import en
import re
import nltk

class Grammer_Analysis_2(object):

	#sentence = None

	def __init__(self, sentence):

		self.string = sentence.lower()

	# returns the class sentence	
	def get_sentence(self):
	
		return self.string

	# finds the subject of the sentence	
	def find_subject(self):
		
		words_list = self.get_sentence().split(" ")

		if words_list[0] == "the":
			subject = 'the ' + words_list[1]
		elif words_list[0] == 'a':
			subject = 'a ' + words_list[1]
		elif words_list[0] == 'an':
			subject = 'an ' + words_list[1]
		elif words_list[0] == 'my': # my cat is sick because he ate too many beans
			subject = 'my ' + words_list[1]
		elif words_list[0] == 'there': # There were four basic causes of the Civil War
			subject = self.there_prefix()
		elif words_list[0] == 'here': # here is the book
			subject = self.here_prefix()
		else:
			subject = self.find_subject_2()

		return subject

	# [('here', 'RB'), ('is', 'VBZ'), ('the', 'DT'), ('book', 'NN'), ('.', '.')]	
	def here_prefix(self):

		sen = self.get_sentence()
		words_list = nltk.word_tokenize(sen)
		tagged = nltk.pos_tag(words_list)
		counter = 0
		subject = 0

		for each in tagged:
			if each[1] == 'DT' or each[1] == 'IN': # the/that/this
				for i in range(counter, len(tagged)):
					if tagged[i][1] == 'NN':	
						subject = tagged[i][0]
						return subject
			counter += 1

		return subject

	# finds the subject when the sentence starts with 'there'
	def there_prefix(self):

		sen = self.get_sentence()
		words_list = nltk.word_tokenize(sen)
		tagged = nltk.pos_tag(words_list)
		counter = 0

		for each in tagged:
			if each[1] == 'IN' or each[1] == 'WDT': # of/for/that/which etc
				subject = tagged[counter-1][0]
			counter += 1	

		return subject

	# finds the subject of the sentence when is is not at the beginning
	def find_subject_2(self):

		sen = self.get_sentence()
		words_list = nltk.word_tokenize(sen)
		tagged = nltk.pos_tag(words_list)
		counter = 0

		for each in tagged:
			if each[1] == 'VB' or each[1] == 'VBD' or each[1] == 'VBG' or each[1] == 'VBN' or each[1] == 'VBP' or each[1] == 'VBZ':
				try: # a fat man landed
					predicate_pos = counter
					subject_pos = counter-1
					subject = tagged[counter-1][0]
					return subject
				except: # an alien landed - the alien is 'VBD'
					subject_pos = counter
					predicate_pos = counter+1
					subject = tagged[counter][0]
					return subject
			counter += 1
			
		return subject	

	# finds the event of the sentence (by appendind the subject and the predicate)	
	def find_predicate(self):

		sen = self.get_sentence()
		words_list = nltk.word_tokenize(sen)
		tagged = nltk.pos_tag(words_list)
		counter = 0
		event = 0

		for each in tagged:
			if each[1] == 'VB' or each[1] == 'VBD' or each[1] == 'VBG' or each[1] == 'VBN' or each[1] == 'VBP' or each[1] == 'VBZ':
				try: # a fat man landed
					predicate = tagged[counter][0]
					return predicate
				except: # an alien landed - the alien is 'VBD'
					predicate = tagged[counter+1][0]
					return predicate
			counter += 1	
			
		return event	

	# finds the event of the sentence (by appendind the subject and the predicate)	
	def find_event(self):

		sen = self.get_sentence()
		words_list = nltk.word_tokenize(sen)
		tagged = nltk.pos_tag(words_list)
		counter = 0
		event = 0

		for each in tagged:
			if each[1] == 'VB' or each[1] == 'VBD' or each[1] == 'VBG' or each[1] == 'VBN' or each[1] == 'VBP' or each[1] == 'VBZ':
				try: # a fat man landed
					predicate_pos = counter
					subject_pos = counter-1
					event = tagged[counter-1][0] + ' ' + tagged[counter][0]
					return event
				except: # an alien landed - the alien is 'VBD'
					subject_pos = counter
					predicate_pos = counter+1
					event = tagged[counter][0] + ' ' + tagged[counter+1][0]
					return event
			counter += 1	
			
		return event
	
	# finds the reason for the event
	def find_reason(self):
	
		sen = self.get_sentence()
		words_list = nltk.word_tokenize(sen) # make list of words

		counter = 0
		reason_list = []

		for each in words_list:
			try:
				if each == 'because' or (each == 'as' and words_list[counter+1] == 'a' and words_list[counter+2] == 'result' and words_list[counter+3] == 'of')\
				or (each == 'due' and words_list[counter+1] == 'to' and words_list[counter+2] == 'the'):
					if words_list[counter-1] == 'not':
						counter += 1
						continue
					for i in range(counter, len(words_list)):
						reason_list.append(words_list[i])
					reason = ' '.join(reason_list)
					return reason
				counter += 1
			except:
				return False	

		reason = ' '.join(reason_list)

		return reason

	# finds the event of the sentence (by appendind the subject and the predicate)	
	def find_new_event(self, sen):

		words_list = nltk.word_tokenize(sen)

		tagged = nltk.pos_tag(words_list)
		counter = 0
		event = 0

		for each in tagged:
			if each[1] == 'VB' or each[1] == 'VBD' or each[1] == 'VBG' or each[1] == 'VBN' or each[1] == 'VBP' or each[1] == 'VBZ':
				try: # a fat man landed
					predicate_pos = counter
					subject_pos = counter-1
					event = tagged[counter-1][0] + ' ' + tagged[counter][0]
					return event
				except: # an alien landed - the alien is 'VBD'
					subject_pos = counter
					predicate_pos = counter+1
					event = tagged[counter][0] + ' ' + tagged[counter+1][0]
					return event
			counter += 1	
			
		return event
	
	# finds the reason for the event
	def find_new_reason(self, sen):

		words_list = nltk.word_tokenize(sen) # make list of words

		counter = 0
		reason_list = []

		for each in words_list:
			if each == 'because':
				for i in range(counter, len(words_list)):
					reason_list.append(words_list[i])
			counter += 1

		reason = ' '.join(reason_list)

		return reason	
	"""	
	# determines wheather the new sentence is corroborative (returns 1),weakens(-1) or has no affect on the class sentence(returns 0)	
	def reference_relations(self, sentence):

		class_sentence = self.get_sentence()

		old_event = self.find_event()
		new_event = self.find_new_event(sentence)

		old_reason = self.find_reason()
		new_reason = self.find_new_reason(sentence)

		return self.compare_strings(old_reason, new_reason)

	# finds level of similarity between two sentences	
	def compare_strings(self, sen1, sen2):

		old_words_list = nltk.word_tokenize(sen1) # make list of words
		new_words_list = nltk.word_tokenize(sen2) # make list of words

		level = 0

		for each1 in old_words_list:
			for each2 in new_words_list:
				if each1 == each2:
					level += 1

		if level == len(old_words_list) or level == len(new_words_list): # same reason
			return 1

		if level > ((len(old_words_list) + len(new_words_list)) / 2) / 2: # the reason sentence starts the same but the object (reason itself) is different
			return -1

		if level == 0: # no connection
			return 0

		return 0
	"""	
	# determines wheather the new sentence is corroborative (returns 1),weakens(-1) or has no affect on the class sentence(returns 0)	
	def reference_relations(self, d):

		class_sentence = self.get_sentence()

		print d.get_sentence()
	
		old_event = self.find_event()
		new_event = self.find_new_event(sentence)

		print "old_event:", old_event
		print "new_event", new_event

		old_reason = self.find_reason()
		new_reason = self.find_new_reason(d.get_sentence())

		print "old_reason:", old_reason
		print "new_reason:", new_reason
		
		return self.compare_strings(old_reason, new_reason)
		
	# finds level of similarity between two sentences	
	def compare_strings(self, sen1, sen2):

		old_words_list = nltk.word_tokenize(sen1) # make list of words
		new_words_list = nltk.word_tokenize(sen2) # make list of words

		level = 0

		for each1 in old_words_list:
			for each2 in new_words_list:
				if each1 == each2:
					level += 1

		if level == len(old_words_list) or level == len(new_words_list): # same reason
			return 1

		if level > ((len(old_words_list) + len(new_words_list)) / 2) / 2: # the reason sentence starts the same but the object (reason itself) is different
			return -1

		if level == 0: # no connection
			return 0

		return 0	

if __name__ == "__main__":

	#c = Grammer_Analysis_2("a man Landed in my back yard yesterday")
	#c = Grammer_Analysis_2("she met him yesterday in the park because she was hungry")
	#c = Grammer_Analysis_2("yesterday my cat was sick because he ate too many beans")
	#c = Grammer_Analysis_2("my cat is sick because he ate too many beans")
	#c = Grammer_Analysis_2("this girl's car is very fancy because she stole it from a rich lady")
	#c = Grammer_Analysis_2("There were four basic causes that started the Civil War")
	#c = Grammer_Analysis_2("Here is the book")
	#c = Grammer_Analysis_2("the heavy traffic is caused not because of the aliens but due to the massive heat")
	c = Grammer_Analysis_2("people in russia would rather eat peaches because they are cheaper")
	
	sentence = c.get_sentence()
	#print sentence
	words_list = nltk.word_tokenize(sentence)
	tagged = nltk.pos_tag(words_list)
	#print tagged
	#print c.find_subject()
	#print c.find_predicate()
	#print c.find_event()
	#print c.find_reason()

	#d = Grammer_Analysis_2("recent studies show that peaches in russia are cheaper")
	#d = Grammer_Analysis_2("in russia, the amount of peaches is smaller than the amount of apples")
	#print c.reference_relations(d)
	
	read_expr = nltk.sem.Expression.fromstring
	expr = read_expr('walk(angus)', type_check=True)
	print expr.argument
	print expr.argument.type
	print expr.is_atom()
	print expr.function
	print expr.function.type
	#print dir(expr)
	sig = {'walk': '<e, t>'}
	expr = read_expr('walk(angus)', signature=sig)
	print expr.function.type
	read_expr = nltk.sem.Expression.fromstring
	print read_expr('dog(cyril)').free()
	print read_expr('dog(x)').free()


		
	
