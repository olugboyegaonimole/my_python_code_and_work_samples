
#OPEN THE FILE

filename = input('enter filename: ')

file = open(filename, encoding="UTF-8")

#TOTAL WORD COUNT IS LOWER THAN EXPECTED. SOLUTIONS:
#1. USE ANOTHER TYPE OF ENCODING
#2. OR OPEN 98-0 FILE USING ANOTHER FILE EXTENSION

print(file)







#CREATE A DICTIONARY TO HOLD THE CONTENTS OF THE FILE

dict1={}







#OPEN YOUR EXCLUSION LIST
stopword = set(word.strip() for word in open("stopwords.txt"))


#print(stopword)






#CREATE A LOOP TO RAED THE DATA

for word in file.read().lower().split():



	#CLEAN DATA

	word = word.replace(",", "")
	word = word.replace("“", "")
	word = word.replace("\"", "")
	word = word.replace(".", "")


	if word not in stopword:



		#ADD TO THE DICT

		if word not in dict1:

			dict1[word] = 1

		else:

			dict1[word] +=1
			


'''
#CHECK FOR WHATS IN THE DICTIONARY
for i,j in dict1.items():
	print(i, ",", j)
'''










#CREATE A LIST TO HOLD THE WORDS IN THE DICTIONARY. USING THE LIST, THE ITEMS CAN BE SORTED AND COUNTED

list1=[]



#TRANSFER THE WORDS TO THE LIST, ONE WORD AT A TIME

for i,j in dict1.items():

	list1.append(i)


'''
#CHECK WHATS IN THE LIST
for i in list1:
	print(i)
'''










'''
#IMPORT THE COLLECTIONS MODULE

#import collections



#ACCESS THE COUNTER METHOD IN THE COLLECTIONS MODULE
#PASS THE DICTIONARY INTO THE METHOD AND ASSIGN IT TO A VARIABLE

#tally = collections.Counter(dict1)



#COUNT AND PRINT OUT THE 10 MOST FREQUENTLY OCCURING ITEMS IN THE DICT

for word, count in (tally.most_common(10)):
	print(word, ",", count)


'''







'''
#THIS IS TO CHECK IF THE TALLY OPERATION BELOW ACHIEVES THE DESIRED OBJ
#IMPORT THE COLLECTIONS MODULE

import collections


#ACCESS THE COUNTER METHOD IN THE COLLECTIONS MODULE
#ASSIGN THE COUNTER METHOD TO A TALLY VARIABLE

tally = collections.Counter()


#LOOP THROUGH THE LIST AND COUNT THE FREQUENCY OF EACH ITEM

for i in list1:
	
	tally[i] += 1
	
	print(i, tally[i])

print(tally)
'''

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    








#IMPORT THE COUNTER MODULE

from collections import Counter



#COUNT AND PRINT OUT THE 10 MOST FREQUENTLY OCCURING ITEMS IN THE LIST

for word, count in (Counter(dict1).most_common(10)):
	print(word, ",", count)
