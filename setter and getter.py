class Animal():

	def __init__(self, color, diet):
		self.color = color
		self.diet = diet
		self.counter = 0
		self._cover = False	#initial value of property, set to anything: float, empty string, int, str, boolean

	
	#property getter
	@property
	def cover(self):
		if self.counter == 0:
			self._cover = 'glass'

		if self.counter == 1:
			self._cover = 'hair'
		
		if self.counter == 2:
			self._cover = 'mink'
		
		if self.counter == 3:
			self._cover = 'skin'
		
		if self.counter == 4:
			self._cover = 'scales'
		
		if self.counter > 4:
			self._cover = 'stone'
		
		return self._cover


	#property setter
	@cover.setter
	def cover(self, value):
		self.counter = value



bee = Animal('yellow', 'straw')

print(bee.cover) #anytime you ask for the value of the property, the program goes to the getter
print(bee.cover)
print(bee.cover)
print(bee.cover)
print(bee.cover)
print()



def swat_bee():
	bee.counter += 1
	bee.cover = 9 #anytime you assign a value to the property, the value is passed as an argument to the setter (so here 9 is passed as an argument to the setter and is assigned to self.counter)
	bee.cover = 4 #this statement calls the setter and assigns 4 to self.counter
	#bee.counter = 3 #this statement calls the setter(does it call the setter?) and assigns 3 to self.counter


for i in range(10):

	print(bee.counter)
	print(bee.cover) #anytime you ask for the value of the property, the program goes to the getter
	print(bee.counter)


	swat_bee()

	print(bee.counter)
	print(bee.cover) #anytime you ask for the value of the property, the program goes to the getter
	print(bee.counter)
