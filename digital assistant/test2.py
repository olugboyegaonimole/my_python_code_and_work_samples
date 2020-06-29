"""
test = "         the quick brown dog jumped "
print(len(test))

test = test.strip(" ")
print(len(test))

test = test.split(" ")
print(test)

"""


test = "the quick brown fox"

test = test.split(" ")

test = " ".join(test[2:])

print(test)