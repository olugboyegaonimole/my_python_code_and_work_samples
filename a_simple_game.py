

#A SIMPLE GAME
class Football():

	class_name=''
	description='' #THIS IS THE INITIAL VALUE OF THE PROPERTY
	objects={}

    #1. WHEN A SETTER IS USED, YOU MUST ASSIGN AN INITIAL VALUE TO THE PROPERTY
    #2. HERE FOR EXAMPLE, THE ASSIGNMENT TAKES PLACE WHEN THE PROPERTY IS DEFINED AS A CLASS ATTRIBUTE


	def __init__(self, name):
		self.name = name
		Football.objects[self.class_name]=self

	def get_description(self):
		print(self.class_name + '\n' + self.description)

class Striker(Football):
	class_name = 'striker'
	description='scores goals'

class Defender(Football):
	class_name='defender'
	description='stops striker'

class Ball(Football):
	def __init__(self, name):
		self.class_name='ball'
		self._description='hollow spherical inflated with air'
		self.status=0
		super().__init__(name)

	@property
	def description(self): #THIS IS THE GETTER
		if self.status==0:
			self._description='hollow spherical inflated with air'
		elif self.status==1:
			self._description = 'you beat one defender!'
		elif self.status==2:
			self._description = 'you beat another defender!'
		elif self.status==3:
			self._description = 'now you beat the goalkeeper!'
		elif self.status>3:
			self._description = 'IT\'S IN THE BACK OF THE NET!!!!!! GOALLLLLLLLLLLLLLLLLLLL!!!!!!!!!!!!!!!'
		return self._description #WHEN A SETTER IS USED THE GETTER MUST RETURN THE PROPERTY ITSELF (AND NOT RETURN A LITERAL VALUE)

    #THE SETTER DIRECTLY ASSIGNS A VALUE TO THE PROPERTY, OR IT ASSIGNS A VALUE TO SOMETHING THAT WILL DETERMINE THE VALUE OF THE PROPERTY
	@description.setter 
	def description(self, value): #THIS IS THE SETTER
		self.status = value #HERE, THE SETTER ASSIGNS A VALUE TO SOMETHING THAT WILL DETERMINE THE VALUE OF THE PROPERTY
		


striker1 = Striker('yekini')
defender1=Defender('uche')
ball01=Ball('addidas')

i=0
def get_input():

	global i

	i += 1

	command = (input('enter command: ')).split(' ')

	verbword = command[0]
	if verbword in verbdict:
		verb = verbdict[verbword]
	else:
		print('unknown')
		return

	if len(command)>1:
		nounword = command[1]
		verb(nounword)
	else:
		verb('nothing')

def say(noun):
	print('you said {}'.format(noun))

def examine(noun):
	if noun in Football.objects:
		Football.objects[noun].get_description()
	else:
		print('there is no {} here'.format(noun))

def kick(noun):
	if noun in Football.objects:
		item = Football.objects[noun]
		if type(item) == Ball:
			item.status += 1
			if item.status == 1:
				print('you kicked the ball!')
			if 2<= item.status <=3:
				print('you kicked the ball again!')
			elif item.status>3:
				print('YOU\'VE SCORED!!!!!!!!!!!')

		else:
			print('you can\'t kick that')
	else:
		print('you can\'t kick that')

verbdict={'say':say, 'examine':examine, 'kick':kick}

while True:
#while i<10:
	get_input()
