#open the file
file1 = open('tom.txt', encoding="utf-8")

file2 = open('voltron.txt', encoding="utf-8")





#create the dicts
dic1={}
dic2={}



#read file1
for word in file1.read().lower().split():


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




	if word == 'cartoon':

		if word not in dic1:
			dic1[word] = 1
		else:
			dic1[word] +=1






#read file2
for word in file2.read().lower().split():


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




	if word == 'cartoon':

		if word not in dic2:
			dic2[word] = 1
		else:
			dic2[word] +=1






from collections import Counter



#d = Counter(dic)


print('tom and jerry', dic1)
print('voltron', dic2)