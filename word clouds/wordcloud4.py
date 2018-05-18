


#open file

file = open("spidey.txt", encoding="utf-8")






#create dict to hold file contents

dict1={}





#read file, lower everything, split into words

for word in file.read().lower().split():
	
	
	#check success
	#print (word)
	



	#clean data

	'''
	word = word.replace("^", "")
	word = word.replace(",", "")
	word = word.replace("“", "")
	word = word.replace("\"", "")
	word = word.replace(".", "")
	word = word.replace("(", "")
	word = word.replace(")", "")
	word = word.replace("[", "")
	word = word.replace("]", "")
	word = word.replace("--", "")
	word = word.replace("”", "")
	'''




	#add to dict

	if word not in dict1:
		dict1[word] = 1
	else:
		dict1[word] += 1






#import collections

from collections import Counter




#create counter method, pass the dictionary into the method

d = Counter(dict1)






#count most commom words

for word, count in d.most_common(30):
	print(word, ":", count)

