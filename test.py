class Vehicle():

	vehicles={}



	#constructor
	def __init__(self, kind, speed, material, substance): #MATERIAL WILL NOT BE ASSIGNED WHEN AN OBJECT IS CREATED
		self.kind = kind
		self.speed = speed
		self.material = material #BECAUSE A GETTER AND A SETTER ALREADY HAVE THIS NAME, THIS ASSIGNMENT WILL BE IGNORED
		self.substance = substance
		self.status=0
		self._integrity = 'intact' #INITIAL VALUE OF THE PROPERTY
		Vehicle.vehicles[self.kind] = self




	#getter
	@property
	def material(self): #THE GETTER AND SETTER NEED NOT HAVE THE SAME NAME AS THE PROPERTY
		if self.status==0:
			self._integrity='intact'
		
		elif self.status==1:
			self._integrity='integrity 75%'

		elif self.status==2:
			self._integrity='integrity 50%'

		elif self.status==3:
			self._integrity='integrity 25%'

		elif self.status==4:
			self._integrity='compromised'

		return self._integrity



	#setter
	@material.setter
	def material(self, value): #THE GETTER AND SETTER NEED NOT HAVE THE SAME NAME AS THE PROPERTY

		self.status = value #THE SETTER IS CALLED AT ANY POINT IN THIS CODE WHERE YOU TRY TO ASSIGN A VALUE TO SELF.STATUS

		return 'test' #setter won't return this
		print('test') #setter won't print this


car1 = Vehicle('sports', 600, 'steel', 'tin') #STEEL IS NOT ASSIGNED TO MATERIAL, NEVERTHELESS 4 ARGUMENTS ARE MANDATORY HERE


print(car1.kind)
print(car1.speed)
print(car1.material) #RATHER THAN CALL THE MATERIAL ATTRIBUTE, THIS WILL CALL THE MAETRIAL PROPERTY
print(car1.substance)



def crash(item):

	item.status += 1 #THIS ATTEMPTS TO ASSIGN A VALUE TO A VARIABLE IN THE SETTER, AND THEREFORE CALLS THE SETTER

	print(car1.material)



def getinput():

	command = (input('enter command:')).split(' ')

	verbword = command[0]

	if verbword in verbdict:
		verb = verbdict[verbword]

	else:
		print('you can\'t do that')
		return


	if len(command)>1:

		noun = command[1]

		myarg = Vehicle.vehicles[noun]

		#command[0](myarg) #WRONG. COMMAND[0] IS A STRING. A STRING ISN'T CALLABLE

		verb(myarg)




verbdict={'crash':crash}


while True:
	getinput()