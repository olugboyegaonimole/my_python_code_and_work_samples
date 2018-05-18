#open the file
file = open('spidey.txt', encoding="utf-8")



#create a data structure to hold its contents
dic={}





#read in the file
for word in file.read().lower().split():


	#clean the words
	word = word.replace("“", "")
	word = word.replace("”", "")
	word = word.replace("\"", "")
	word = word.replace(".", "")
	word = word.replace(",", "")
	'''
	word = word.replace("", "")
	word = word.replace("", "")
	word = word.replace("", "")
	word = word.replace("", "")
	'''

	if word == "keaton":

		if word not in dic:
			dic[word] = 1
		else:
			dic[word] +=1



	if word == "spider-man":

		if word not in dic:
			dic[word] = 1
		else:
			dic[word] +=1



	if word == "watts":

		if word not in dic:
			dic[word] = 1
		else:
			dic[word] +=1



	if word == "parker":

		if word not in dic:
			dic[word] = 1
		else:
			dic[word] +=1


	if word == "harrier":

		if word not in dic:
			dic[word] = 1
		else:
			dic[word] +=1

	if word == "holland":

		if word not in dic:
			dic[word] = 1
		else:
			dic[word] +=1


for i,j in dic.items():
	print(i,j)



from collections import Counter



d = Counter(dic)


for word, something in d.most_common(6):
	print(word, ",", something)



