#!/usr/bin/env python

#creator: Shay Avrahami

import re # regex
from HTMLParser import HTMLParser


vowels = 	['a', 'e', 'i', 'o', 'u']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']      

class Parsing_indexer(object):

	def trim_ies(self, val):
		
		# remove the 'ies' and add 'y' (laities)
		val = val[:-3]
		val += "y"

		return val

	def trim_es(self, val):

		# if befor the 'es' there is 's', 'x', 'z', 'sh' or 'ch' - remove 'es' (buses)
		if re.search("^([a-z]+)(s|x|z|sh|ch)es$", val):
			val = val[:-2]

		return val	

	def trim_s(self, val):

		flag = False
		ok_s_suffix = ["crisis", "crises", "always", "nowadays", "sometimes", "wurzels" \
	                   "javas", "bus", "abs", "ups", "mass", "yes", "gas", "ass", "kiss", "sos"]

		for x in ok_s_suffix:
			if x == val:
				flag = True
				break

		if(flag == False):
	    	# if before the 's' there is a 'y' and before it a vowel - delete the 's' (jerseys)
			if re.search("^([a-z]+)(a|e|o|u|i)ys$", val):
				val = val[:-1]
				flag = True

		# general case - delete the 's'
		if flag == False:
			val = val[:-1]

		return val

	def trim_d(self, val):

		flag = False
		ok_d_suffix = ["quad", "quid", "quod", "bawd", "wind", "bund", "chid", "fund", \
	                     "kind", "veld", "vend", "avid", "bald", "band", "baud", "bend", \
	                     "bind", "bold", "bond", "bird", "clad", "clod", "cold", "crud", \
	                     "curd", "fend", "feud", "find", "fold", "fond", "lewd", "maud", \
	                     "meld", "mend", "mild", "mind", "mold", "plod", "pond", "scud", \
	                     "skid", "spud", "void", "wand", "weld", "wend", "wild", "wold", \
	                     "acid", "amid", "bard", "bead", "bird", "brad", "card", "cord", \
	                     "dyad", "fard", "food", "ford", "gaud", "geld", "gold", "hand", \
	                     "held", "hind", "hold", "maid", "mead", "mood", "paid", "pard", \
	                     "prod", "thud", "ward", "woad", "wood", "word", "auld", "egad", \
	                     "gird", "goad", "good", "grid", "hard", "head", "herd", "hood", \
	                     "land", "laud", "lend", "loud", "nurd", "rudd", "shad", "shod", \
	                     "sudd", "yard", "dead", "laid", "lard", "lead", "load", "lord", \
	                     "nard", "nerd", "rand", "redd", "rend", "rind", "sand", "send", \
	                     "sild", "slid", "sold", "stud", "surd", "tend", "arid", "raid", \
	                     "read", "road", "rood", "sard", "sord", "toad", "trad", "trod", \
	                     "thread", "bud", "cud", "fud", "kid", "mud", "vid", "bad", "bid", \
	                     "bod", "cad", "cod", "fad", "fid", "mad", "mid", "mod", "pad", "pod", \
	                     "wad", "dud", "gad", "god", "had", "hod", "add", "and", "dad", "did", \
	                     "eld", "end", "lad", "lid", "nod", "odd", "old", "oud", "aid", "rad", \
	                     "rid", "rod", "sad", "sod", "tad", "tod"]

		for x in ok_d_suffix:
			if x == val:
				flag = True
				break

	    # general case - remove the 'd'		
		if flag == False:
			val = val[:-1]

		return val

	def trim_ed(self, val):
		if val == "travelled":
			print "entering trim_ed with token", val

		flag = False
		length = len(val)
		ok_ed_suffix = ["emplaced", "untapped", "wormseed", "berobed", "sacred", "cooed", "teed", "ted", "sned", "fed", "bed", "reed", "need", "sled", "pied", "seed", "meed", "oped", "feed", "hued", "abed", "coed", "weed", "shed", "toed"]
						
		                                                                                                                                                                                
		for x in ok_ed_suffix:
			if x == val:
				flag = True
				break

		# past tense verbs - remove 'ied' and add 'y'		
		if flag == False:
			past_tense = ["applied", "babied", "bullied", "carried", "copied", "cried", \
						"dried", "fried", "horrified", "hurried", "magnified", "married", \
						"muddied", "occupied", "partied", "pried", "replied", "satisfied", \
						"scurried", "shied", "spied", "studied", "supplied", "terrified", \
						"tidied", "tried", "unified", "worry"]

			for x in past_tense:
				if x == val:
					val = val[:-3]
					val += "y"
					flag = True
					break

		# exceptions
		if flag == False:
			if( (val == "inherited") or (val == "inhibited") or (val == "visited") ):
				val = val[:-2]
				flag = True
				
		# 1 : if before the 'ed' there is a 'y' - remove 'ed' (played)
		if flag == False:
			if length > 4:
				if re.search("^([a-z]+)yed$", val):
					#if val == "travelled":
					#	print "trim_ed case 1 ------------------------ the token is", val
					val = val[:-2]
					flag = True			

		# 2	: if before the 'ed' there is a 'i' - remove only the 'd' (lied)
		if flag == False:
			if length > 3:
				if re.search("^([a-z]+)ied$", val):
					#if val == "travelled":
					#	print "trim_ed case 2 ------------------------ the token is", val
					val = val[:-1]				
					flag = True			
					
		# 3 : if before the 'ed' there are 2 different consonants and the second consonant isn't 'k' - remove only the 'd' (danced)
		flag_cons1 = False
		flag_cons2 = False
		if flag == False:
			if length > 4:
				for x in consonants:
					if x == val[length-3]:
						flag_cons1 = True
				for x in consonants:
					if x == val[length-4]:
						flag_cons2 = True	

				if flag_cons1 and flag_cons2 and val[length-3] != "k" and (val[length-3] != val[length-4]):
					#if val == "travelled":
					#	print "trim_ed case 3 ------------------------ the token is", val	
					val = val[:-1]				
					flag = True														

		# 4 : if before the 'ed' there is consonant vowel consonant - remove the 'd' (smiled, baked)
		if flag == False:
			if length > 4:
				if re.search("^([a-z]*)([b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z][a|e|i|o|u][b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z])ed$", val):
					#if val == "travelled":
					#	print "trim_ed case 4 ------------------------ the token is", val					
					val = val[:-1]
					flag = True			
					
		# 5 :  if before the 'ed' there are two identical letters and before it:
		# 	   consonant vowel consonant (which is the first duplicate letter) - remove the 'ed' and the second duplication (stopped, tapped)
		flag_cons1 = False
		flag_cons2 = False
		flag_vowel1 = False
		if flag == False:
			if length > 5:		
				if val[length-3] == val[length-4]:

					for x in consonants:
						if x == val[length-4]:
							flag_cons1 = True

					for x in vowels:
						if x == val[length-5]:
							flag_vowel1 = True

					for x in consonants:
						if x == val[length-6]:
							flag_cons2 = True

					if flag_cons1 and flag_cons2 and flag_vowel1:
						#if val == "travelled":
						#	print "trim_ed case 5 ------------------------ the token is", val
						val = val[:-3]
						flag = True				

		# 6 : if the basic root ends with 'c' - a 'k' was added before 'ed' (picnicked, mimicked)
		if flag == False:
			if length > 4:
				if re.search("^([a-z]+)cked$", val):
					#if val == "travelled":
					#	print "trim_ed case 6 ------------------------ the token is", val
					val = val[:-3]
					flag = True

		# 7 : 4 letters verbs that ends with 'ye' - remove only the 'd' (dyed)
		if flag == False:
			if length == 4:
				if re.search("^([a-z]+)yed$", val):
					#if val == "travelled":
					#	print "trim_ed case 6 ------------------------ the token is", val
					val = val[:-1]				
					flag = True

		# 8 : verbs ending in 'ee', 'ye' and 'oe' - remove only the 'd' at the end (freed)
		if flag == False:
			if length > 3:
				if re.search("^([a-z]+)eed$", val) or re.search("^([a-z]+)yed$", val) or re.search("^([a-z]+)oed$", val):
					#if val == "travelled":
					#	print "trim_ed case 8 ------------------------ the token is", val
					val = val[:-1]
					flag = True

		# 9: general case - remove the 'ed' at the end of the val (opened)
		if flag == False:
			if length > 3:
				#if val == "travelled":
				#		print "trim_ed general case ------------------------ the token is", val
				val = val[:-2]

		return val
		
	# remove 'fully' suffix (irefully)
	def trim_fully(self, val):

		if len(val) > 5:
			val = val[:-5]

		return val

	def trim_ly(self, val):

		flag = False
		length = len(val)
		ok_ly_suffix = ["ally", "alley", "anomaly", "apply", "assembly",
	                      "barfly", "belly", "blowfly", "botfly", "bully", "burly", "busily", "butterfly",
	                      "billy", "comply", "dally", "doily", "dolly", "dragonfly", "duly"
	                      "elly", "family", "firefly", "fly", "gadfly", "gully",
	                      "hillbilly", "holly", "homily", "horsefly",
	                      "imply", "jelly", "jilly" , "lily",
	                      "mayfly", "medfly", "molly", "monopoly", "multiply",
	                      "nelly", "outfly", "panoply", "ply", "potbelly",
	                      "rally", "rely", "reply",
	                      "sally", "sly",  "supply", "syndactyly",
	                      "tally", "underbelly", "willy", "wryly"]

		for x in ok_ly_suffix:
			if x == val:
				flag = True
				break
				
	# exceptions
		if (val == "shyly") or (val == "slyly") or (val == "coyly") or (val == "greyly") or (val == "friendly"):
			val = val[:-2]
			flag = True

	    # 1 - if the suffix is 'cally' - remove the cally (problematically, specifically)
		if flag == False:
			if length > 5:
				if re.search("^([a-z]+)cally$", val):
					val = val[:-4]
					#print "trim ly case 1, token is", val
					flag = True

	    # 2 - if there is a consonant (except 'l') before the 'ly' - remove the 'y' and add 'e' (simply, humbly)
		if flag == False:
			if re.search("^([a-z]+)([b|c|d|f|g|h|j|k|m|n|p|q|r|s|t|v|w|x|y|z])ly$", val):
				val = val[:-1]
				val += "e"
				flag = True
				#print "trim ly case 2, token is", val

	    # 3 - if there is a vowel (except 'u' or 'i') before the 'ly' - remove the 'ly' (agilely)
		if flag == False:
			if re.search("^([a-z]+)([a|e|o])ly$", val):
				val = val[:-2]
				flag = True
				#print "trim ly case 3, token is", val

	    # 4 - if the token ends in 'lly' but it's not 'cally' - remove the 'y' (shrilly, fully)
		if flag == False:
			if length > 4:
				if re.search("^([a-z]+)lly$", val) and val[length-4] != "a":
					val = val[:-1]
					flag = True
					
	    # 5 - if before 'ly' there is 'u' - remove the 'ly' and put 'e' (duly, truly)
		if flag == False:
			if re.search("^([a-z]+)uly$", val):
				val = val[:-2]
				val += "e"
				flag = True

	    # 6 - if before 'ly' there is 'i' - remove the 'ly' and turn the 'i' to 'y' (busily, easily)
		if flag == false:
			if re.search("^([a-z]+)ily$", val):
				val = val[:-3]
				val += "y"
				flag = True

	    # 7 - general case - remove the 'ly' suffix 	
		if flag == False:
			val = val[:-2]

		return val
		
	def trim_ing(self, val):
		#print "entering trim_ing with token ", val

		flag = False
		length = len(val)
		ok_ing_suffix = ["bling", "building", \
		                    "ding", "dorking", \
		                    "ending", "evening", "everything", \
		                    "fling", \
		                    "gloaming", \
		                    "king", \
		                    "meeting", "ming" \
		                    "nothing", \
		                    "painting", "ping", \
		                    "ring", \
		                    "scaffolding", "something", "spring", "string", \
		                    "thing", \
		                    "wing"]

		for x in ok_ing_suffix:
			if x == val:
				flag = True

		# 1 - if before the 'ing' there is a multiplied letter and before it a vowel -
		# remove the 'ing' and the second multiplied letter (stopping, wrapping)
		if flag == False:
			if length > 6:
				if val[length-4] == val[length-5]:

					for x in vowels:
						if x == val[length-6]:
							val = val[:-4]
							#print "-----------------trim_ing case 1 token is", val
							flag = True
							

		# 2 - if before the 'ing' there is 'ee' - just remove the 'ing' (seeing)
		if flag == False:
			if length > 5:
				if re.search("^([a-z]+)eeing$", val):
					val = val[:-3]
					#print "-----------------trim_ing case 2 token is", val
					flag = True

		# 3 - if before the 'ing' there is a 'y' - remove the 'ying' and add 'ie' (dying) 
		if flag == False:
			if length > 4:
				if re.search("^([a-z]+)ying$", val):
					val = val[:-4]
					val += "ie"
					#print "-----------------trim_ing case 3 token is", val
					flag = True

		# 4 - if before the 'ing' there is consonant vowel consonant -
		# remove 'ing' and add 'e' (making)	
		#^([a-z]+)		
		if flag == False:
			if length > 5:
				if re.search("^([a-z]*)([b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z])([a|e|i|o|u])([b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z])ing$", val):
					val = val[:-3]
					val += "e"
					flag = True
					#print "-----------------trim_ing case 4 token is", val

		# general case - remove the 'ing' suffix 			
		if flag == False:
			val = val[:-3]
			#print "-----------------trim_ing general case token is", val

		return val
		
	def trim_ious(self, val):

		flag = False
		ok_ious_suffix = [  "cautious", "conscious", "curious", \
		                    "delicious", \
		                    "envious", \
		                    "hilarious", \
		                    "nutritious", \
		                    "obvious", \
		                    "previous", \
		                    "serious", \
		                    "tedious"]

		for x in ok_ious_suffix:
			if x == val:
				flag = True
				break

		# general case - remove the 'ious' suffix
		if flag == False:
			val = val[:-4]

		return val
		
	def trim_ssion(self, val):

		flag = False
		length = len(val)

		ok_ssion_suffix = [ "abscission", "accession", \
		                    "cession", "compassion", "concession", "conscious", "curious", \
		                    "concession", "concussion" \
		                    "decommission", "delicious", "demission", "dispassion", \
		                    "egression", "envious", \
		                    "fission", \
		                    "hilarious", \
		                    "immunosuppression", "intercession", "intermission", "intersession",\
		                    "introgression", "intromission", \
		                    "manumission", "mission", \
		                    "neurotransmission", \
		                    "obsession", "obvious", "oppression", \
		                    "passion", "percussion", "photoemission", "precession", \
		                    "procession", "profession", \
		                    "readmission", "recession", "reimpression", "remission",  \
		                    "repercussion", "rescission", "resubmission", "retransmission", \
		                    "retrocession", \
		                    "scission", "secession", "serious", "session", "submission", \
		                    "succession", "supersession",  \
		                    "tedious"]

		for x in ok_ssion_suffix:
			if x == val:
				flag = True

		# 1 - if before the 'ssion' there is 'mi' - remove the 'ssion' and add 't' (emission)
		if flag == False:
			if length > 7:
				if re.search("^([a-z]+)mission", val):
					val = val[:-5]
					val += "t"
					flag = True
					

		# general case - remove the 'ion' suffix
		if flag == False:
			val = val[:-3]

		return val
	    
	def trim_sion(self, val):

		length = len(val)
		flag = False
		ok_sion_suffix = [ "mansion", \
		                   "pension", \
		                   "version"]

		for x in ok_sion_suffix:
			if x == val:
				flag = True

		# 1 - if before the 'sion' there is an 'l' - remove the 'on' and add 've' (emulsion)		
		if flag == False:
			if length > 5:
				if re.search("^([a-z]+)lsion", val):
					val = val[:-2]
					val += "ve"
					flag = True

		# general case - remove 'ion' and add 'e' (revision)
		if flag == False:
			if length > 4:
				val = val[:-3]
				val += "e"

		return val
		
	def trim_tion(self, val):
		
		# if before 'tion' there is 'a' or 'e' - remove 'ion' and add 'e' (approximation)
		if re.search("^([a-z]+)(a|e)tion$", val): 
			val = val[:-3]
			val += "e"

		return val
		
	def trim_ness(self, val):

		flag = False

		# 1 - if before the 'ness' there is 'i' - remove 'iness' and add 'y' (happiness)
		if re.search("^([a-z]+)iness$", val):
			val = val[:-5]
			val += "y"
			flag = True

		# general case - remove the 'ness' suffix 	
		if flag == False:
			val = val[:-4]

	def trim_ility(self, val):

		flag = False
		val = val[:-5] # this is has to be done in either case

		# if there is a 'b' before 'ility' suffix - remove the 'ility' and add 'le' (sustainability) 
		if re.search("^([a-z]+)bility$", val):
			val += "le"
			flag = True

		# general case - remove the 'ility' suffix and add 'e' (servility)
		if flag == False:
			val += "e"

		return val
		
	def trim_osity(self, val):

		# remove the 'sity' and add 'us' (tortuosity)	
		val = val[:-4]
		val += "us"
		return val

	def trim_ity(self, val):

		flag = False
		# exceptions
		if val == "affinity" or val == "calamity" or val == "heredity":
			flag = True

		# if before the 'ity' there is 'al', 'an', 'ar', 'ic', 'id', 'or' - remove the ity (humidity)
		if flag == False:
			if re.search("^([a-z]+)(al|an|ar|ic|id|or)ity$", val):
				val = val[:-3]

		return val

	def trim_ship(self, val):

		# remove the 'ship' suffix (friendship)
		val = val[:-4]
		return val

	def trim_hood(self, val):

		# remove the 'hood' suffix (falsehood)	
		val = val[:-4]
		return val
		
	def trim_ence(self, val):

		# remove the 'ce' suffix and add 't' (succulence)
		val = val[:-2]
		val += "t"	

	def trim_ful(self, val):

		flag = False
		ok_ful_suffix = ["awful", "artful"]

		if val == "awful" or val == "artful":
			flag = True

		# 1 - if before the 'ful' there is 'i' and before it consonant -
		#     remove the 'iful' and add 'y' (plentiful)
		if re.search("^([a-z]+)([b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z])iful$", val):
			val = val[:-4]
			val += "y"
			flag = True

		# general case - remove the 'ful' suffix
		if flag == False:
			val = val[:-4]

		return val
		
	def trim_est(self, val):

		length = len(val)
		flag = False

		# 1 - if before the 'est' there is a 'i' - remove the 'iest' and add 'y' (healthiest)
		if re.search("^([a-z]+)iest$", val):
			val = val[:-4]
			val += "y"
			flag = True

		# 2 - if before the 'est' there is double consonant, before it a vowel and before it consosnat - 
		# remove the second letter and the 'est' (hottest)
		if flag == False:
			if length > 6:
				if re.search("^([a-z]+)([b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z][a|e|i|o|u][b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z][b|c|d|f|g|h|j|k|l|m|n|p|q|r|s|t|v|w|x|y|z])est$", val):
					val = val[:-4]

		return val

	def trim_less(self, val):

		flag = False	
		# if before the 'less' there is 'i' - remove 'iless' and add 'y' (bodiless)
		if re.search("^([a-z]+)iless$", val):
			val = val[:-5]
			val += "y"
			flag = True

		if flag == False:
			val = val[:-4]

		return val
		
	def trim_en(self, val):

		cut_en_suffix = ["darken", \
		                 "eaten", \
		                 "fallen", \
		                 "golden", \
		                 "weaken"]

		# remove 'en' if the val is one of the 'en' suffix words to cut                 
		for x in cut_en_suffix:
			if x == val:
				val = val[:-2]
				break

		return val		

	def trim_n(self, val):

		cut_n_suffix = ["broken", \
		                "proven", \
		                "seen", "shaken", "stolen", \
		                "taken", \
		                "written"]

		# remove 'n' if the val is one of the 'n' suffix words to cut                 
		for x in cut_n_suffix:
			if x == val:
				val = val[:-1]
				break          

		return val

	# parse the token to remove suffixes and remain with the root
	def parsing(self, val):

		flag = False
		length = len(val)

		m = val.split(":")
		if m is not None:
			if m[0] == "http" or m[0] == "https":
				return val
		
		# trim ies - remove the 'ies' and add 'y' (laities)
		if length > 3:
			if  re.search("^([a-z]+)ies$", val):
					val = self.trim_ies(val)
					flag = True

		# trim es - if befor the 'es' there is 's', 'x', 'z', 'sh' or 'ch' - remove 'es' (buses)
		if(flag == False):
			if length > 3:
				if  re.search("^([a-z]+)es$", val):
					val = self.trim_es(val)
					flag = True

		# trim s - the suffix is 's' but it's not 'ings', 'ious' or 'less' (stands)	
		if(flag == False):
			if length > 3:
				if 	val[length-1] == "s" and val[length-2] != "g" and val[length-2] != "u" and val[length-2] != "s":				
				#if re.search("([a-z]+)$s", val) and not( bool(re.search("([a-z]+)ings", val)) or bool(re.search("([a-z]+)ious", val)) or bool(re.search("([a-z]+)less", val)) ):				
					val = self.trim_s(val)
					flag = True

		# the suffix is 'd' but it's not 'ed' and not 'hood'
		if(flag == False):
			if re.search("^([a-z]+)d$", val) and re.search("^([a-z]+)?!ed$", val) and re.search("^([a-z]+)?!hood$", val): 
				val = self.trim_d(val)
				flag = True
				

		# the suffix is ed
		if(flag == False):
			if(length > 3):
				if re.search("^([a-z]+)ed$", val):
					val = self.trim_ed(val)
					flag = True

		# the suffix is 'fully' (irefully)
		if(flag == False):
			if(length > 3):
				if(re.search("^([a-z]+)fully$", val)):
					val = self.trim_fully(val)
					flag = True

		# the suffix is 'ly'
		if(flag == False):
			if(length > 3):
				if(re.search("^([a-z]+)ly$", val)):
					val = self.trim_ly(val)
					flag = True

		# 'ings' suffix - transformed to 'ing' suffix and go to trim_ing function			
		if(flag == False):
			if length > 4:
				if re.search("^([a-z]+)ings$", val):
					val = val[:-1]
					val = self.trim_ing(val)
					#print "parsing ings suffix"
					flag = True

		# 'ing' suffix
		if(flag == False):
			if length > 3:
				if re.search("^([a-z]+)ing$", val):
					val = self.trim_ing(val)
					flag = True
					
		# 'ious' suffix
		if(flag == False):		
			if length > 4:
				if re.search("^([a-z]+)ious$", val):
					val = self.trim_ious(val)
					flag = True

		# 'ssion' suffix
		if(flag == False):
			if length > 5:
				if re.search("^([a-z]+)ssion$", val):
					val = self.trim_ssion(val)
					flag = True

		# 'sion' suffix
		if(flag == False):
			if length > 5:
				if re.search("^([a-z]+)sion$", val):
					val = self.trim_sion(val)
					flag = True

		# 'tion' suffix
		if(flag == False):
			if length > 5:
				if re.search("^([a-z]+)tion$", val):
					val = self.trim_tion(val)
					flag = True

		# 'ness' suffix
		if(flag == False):
			if length > 5:
				if re.search("^([a-z]+)ness$", val):
					val = self.trim_ness(val)
					flag = True
					
		# 'ility' suffix 
		if(flag == False):
			if length > 5:
				if re.search("^([a-z]+)ility$", val):
					val = self.trim_ility(val)
					flag = True

		# 'osity' suffix
		if(flag == False):
			if length > 4:
				if re.search("^([a-z]+)osity$", val):
					val = self.trim_osity(val)
					flag = True

		# 'ity' suffix
		if(flag == False): 	
			if length > 4:
				if re.search("^([a-z]+)ity$", val):
					val = self.trim_ity(val)
					flag = True

		# 'ship' suffix 			
		if(flag == False):
			if length > 6:
				if re.search("^([a-z]+)ship$", val):
					val = self.trim_ship(val)
					flag = True

		# 'hood' suffix
		if(flag == False):
			if length > 5:
				if re.search("^([a-z]+)hood$", val):
					val = self.trim_hood(val)
					flag = True
					
		# 'ence' suffix	
		if(flag == False):
			if length > 5:
				if re.search("^([a-z]+)ence$", val):
					val = self.trim_ence(val)
					flag = True

		# 'ful' suffix			
		if(flag == False):
			if length > 4:
				if re.search("^([a-z]+)ful$", val):
					val = self.trim_ful(val)
					flag = True

		# 'est' suffix
		if(flag == False):
			if length > 4:
				if re.search("^([a-z]+)est$", val):
					val = self.trim_est(val)
					flag = True

		# 'less' suffix
		if(flag == False):
			if length > 5:
				if re.search("^([a-z]+)less$", val):
					val = self.trim_est(val)
					flag = True

		# 'en' suffix
		if(flag == False):
			if length > 3:
				if re.search("^([a-z]+)en$", val):
					val = self.trim_en(val)
					flag = True
					
		# 'n' suffix
		if(flag == False):
			if length > 3:
				if re.search("^([a-z]+)n$", val):
					val = self.trim_n(val)
					flag = True

		return val

# to strip the html tags, used by the function 'strip_tags'
class MLStripper(HTMLParser):

    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

		  
