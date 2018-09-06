#rest apis for chelseafc.com


#PLAN for chelseafc

#create resource model
#create uris
#create representations
#assign methods
#create api



### create resource model ###

	#collection resources

		#first-team-players
		#coaching-staff

	#singleton resources

		#kepa arizabalaga
		#maurizio sarri
		#striker1
		#striker2
		#striker3
		#striker4
		#striker5
		#striker6

	#sub-collection resources

		#matches-played
		#days at work



### create uris ###

	#for collection resources
		#http://www.chelsea.com/player-management/first-team-players
		#http://www.chelsea.com/staff-management/coaching-staff
		#http://www.chelsea.com/staff-management/academy


	#for singleton resources
		#http://www.chelsea.com/player-management/first-team-players/{id}
		#http://www.chelsea.com/staff-management/coaching-staff/{id}
		#http://www.chelsea.com/staff-management/academy/{id}


	#for sub collection resources
		#http://www.chelsea.com/player-management/first-team-players/{id}/matches-played
		#http://www.chelsea.com/staff-management/coaching-staff/{id}/days-at-work
		#http://www.chelsea.com/staff-management/academy/{id}/days-in-training
		

'''

### create representations ###

# i need to create a database connection between the api and these representations

	#collection resources

		#first-team-players
		<first-team-players size=7>
			<link rel="self" href="/first-team-players"/>


			<first-team-player id="01">
				<link rel="self" href="/first-team-players/01"/>
			</first-team-player>


			<first-team-player id="02">
				<link rel="self" href="/first-team-players/02"/>
			</first-team-player>


			<first-team-player id="03">
				<link rel="self" href="/first-team-players/03"/>
			</first-team-player>


			<first-team-player id="04">
				<link rel="self" href="/first-team-players/04"/>
			</first-team-player>


			<first-team-player id="05">
				<link rel="self" href="/first-team-players/05"/>
			</first-team-player>


			<first-team-player id="06">
				<link rel="self" href="/first-team-players/06"/>
			</first-team-player>


			<first-team-player id="07">
				<link rel="self" href="/first-team-players/07"/>
			</first-team-player>

		</first-team-players>


		#coaching staff

		<coaching-staff size=1>
			<link rel="self" href="/coaching-staff"/>

			<coach id="01"> #does this resource name 'coach' have to be identical to the resource name of every other entity in the coaching-staff collection resource?
							#must the id "01" be an integer or can it be a string?
				<link rel="self" href="/coaching-staff/01"/>
			</coach>

		</coaching-staff>


	#sub-collection resources (full representation)

		#matches played player 01

		<matches-played size=8>
			<link rel="self" href="/first-team-players/01/matches-played"/>


			<match-played id="01">
				<link rel="self" href="/first-team-players/01/matches-played/01"/>
				<link rel="detail" href="/matches-played/01"/>

			</match-played>

		
		</matches-played>



		#days at work staff 01

		<days-at-work size=5>
			<link rel="self" href="/coaching-staff/01/days-at-work"/>

			<day-at-work id="01">
				<link rel="self" href="/coaching-staff/01/days-at-work/01"/>
				<link rel="detail" href="/days-at-work/01"/>

			</day-at-work>


		</days-at-work>



### assign methods ###

	#get
	#post
	#put
	#delete



	#assign get
		#collection resources

		http get /first-team-players
		http get /coaching-staff


		#singleton resources

		http get /first-team-players/{id}
		http get /coaching-staff/{id}


		#sub-colletion resources

		http get /first-team-players/{id}/matches-played
		http get /coaching-staff/{id}/days-at-work

		http get /first-team-players/{id}/matches-played/{id}
		http get /coaching-staff/{id}/days-at-work/{id}


	#assign post
		#collection resources

		http post /first-team-players
		http post /coaching-staff


		#sub-colletion resources	#is this possible?

		http get /first-team-players/{id}/matches-played
		http get /coaching-staff/{id}/days-at-work


	#assign put
		#singleton resources

		http get /first-team-players/{id}
		http get /coaching-staff/{id}


		#singleton resources in sub-colletion resources

		http get /first-team-players/{id}/matches-played/{id}
		http get /coaching-staff/{id}/days-at-work/{id}


	#assign delete	
		#singleton resources

		http get /first-team-players/{id}
		http get /coaching-staff/{id}


		#singleton resources in sub-colletion resources

		http get /first-team-players/{id}/matches-played/{id}
		http get /coaching-staff/{id}/days-at-work/{id}

'''


### create api ###



#PLAN for creating api

	#import libraries
	#create objects (Flask and Api)
	#connect to database (or create database)
	#create resources (collection and singleton)
	#add resources (collection and singleton)
	#run



#IMPORT LIBRARIES

from flask import Flask, request
from flask_restful import Resource, Api 



#CREATE FLASK AND API OBJECTS

app = Flask(__name__)
api = Api(app)



#CONNECT TO DATABASE (OR CREATE DATABASE)

database=[
	{"departmentName":"first-team-players", "departmentId":1, "staffId":1, "staffName":"kepa arizabalaga", "age":23},
	{"departmentName":"first-team-players", "departmentId":1, "staffId":2, "staffName":"victor moses", "age":28},
	{"departmentName":"academy", "departmentId":2, "staffId":3, "staffName":"eden hazard", "age":25},
	{"departmentName":"coaching-staff", "departmentId":3, "staffId":4, "staffName":"maurizio sarri", "age":56},

	]



#CREATE RESOURCES

	#COLLECTION RESOURCES

class ViewDatabase(Resource):

	def get(self):

		return {'the database is': database}



class ViewFirstTeamPlayers(Resource):

	def get(self):

		result = [i for i in database if i["departmentName"]=='first-team-players']

		return {'first-team-players are':result}



class ViewCoachingStaff(Resource):

	def get(self):

		result = [i for i in database if i["departmentName"]=='coaching-staff']

		return {'the coaching staff are': result}



class ViewAcademy(Resource):

	def get(self):

		result = [i for i in database if i["departmentName"]=='academy']

		return {'the academy is': result}



	#SINGLETON RESOURCES



#ADD RESOURCES

	#COLLECTION RESOURCES

api.add_resource(ViewDatabase, '/')

api.add_resource(ViewFirstTeamPlayers, '/first-team-players')

api.add_resource(ViewAcademy, '/academy')

api.add_resource(ViewCoachingStaff, '/coaching-staff')





	#SINGLETON RESOURCES
'''
api.add_resource(ViewKepaArizabalaga, '/first-team-players/1')

api.add_resource(ViewVictorMoses, '/first-team-players/2')

api.add_resource(ViewEdenHazard, '/first-team-players/3')

'''

#RUN

if __name__ == '__main__':
	app.run(debug=True, port=8080)