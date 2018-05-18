#open the file
file = open('tom.txt', encoding="utf-8")





#create a dict
dic={}



#read the file
for word in file.read().lower().split():


	#print(word)



	word = word.replace("“", "")
	word = word.replace("”", "")
	word = word.replace("\"", "")
	word = word.replace(",", "")
	word = word.replace(".", "")
	word = word.replace("", "")
	word = word.replace("", "")
	word = word.replace("", "")
	word = word.replace("", "")
	word = word.replace("", "")




	if word == 'tom':

		if word not in dic:
			dic[word] = 1
		else:
			dic[word] +=1





	if word == 'jerry':

		if word not in dic:
			dic[word] = 1
		else:
			dic[word] +=1



from collections import Counter



d = Counter(dic)


print(dic)