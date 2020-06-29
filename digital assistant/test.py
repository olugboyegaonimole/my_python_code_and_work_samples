test = "who is iouioweuriouwoiu who what where how many are"

print(test)
"""
if "who is " in test:
    test = test.strip("who is ")


print(test)
"""

test = test.split(" ")

print(test)

stopwords = ["is", "who", "what", "where", "why", "when", "how", "many", "are", "the", "a", "was", "were", "did", "which", "will", "be", "would", "could", "should", "can", "shall", "is"]

stopstring = " ".join(stopwords)

print(stopstring)

test = [i for i in test if i not in stopwords]

print(test)