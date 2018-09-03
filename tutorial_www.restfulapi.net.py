#WHAT SHOULD BE YOUR TAKEAWAY FROM THIS EXERCISE?




#SOURCE: https://restfulapi.net/, https://en.wikipedia.org/wiki/Hypermedia


#WHAT IS REST
	#WHAT IS REST
	#GUIDING PRINCIPLES
	#RESOURCES
	#RESOURCE METHODS
	
#REST CONSTRAINTS
	#CLIENT-SERVER SEPARATION
	#GENERALISED COMPONENT INTERFACE 
	#LAYERED SYSTEM
	#STATELESS INTERACTIONS
	#CACHEABLE RESPONSES
	#DOWNLOAD CODE ON DEMAND

#REST RESOURCE NAMING GUIDE
	#USE NOUNS
	#CONSISTENCY IS THE KEY
	#DON'T USE CRUD FUNCTION NAMES IN URIs
	#FILTER URI COLLECTION WITH QUERY COMPONENT

#Guides
	#Caching
	#Compression
	#Content Negotiation
	#HATEOAS
		#what is HATEOAS?
			#hypermedia as the engine of application state
			#implication: hypermedia links returned by the server drive the state of the application


	#Idempotence
	#Security Essentials
	#Versioning
	#Statelessness


#Tech – How To
	#REST API Design Tutorial
	#Create REST APIs with JAX-RS 2.0

#FAQs
	#PUT vs POST
	#N+1 Problem
	#‘q’ Parameter

#Resources
	#Comparing SOAP vs REST APIs
	#HTTP Methods
	#Richardson Maturity Model
	#HTTP Response Codes
	#200 (OK)
	#201 (Created)
	#202 (Accepted)
	#204 (No Content)









#WHAT IS REST

	#what is REST?

		#representational state transfer
		#an architectural style




	#what is it an architectural style for?

		#distributed hypermedia systems




	#what is hypermedia?

		#non-linear medium of information
		#e.g. graphics, audio, video, plain text, hyperlinks





#REST CONSTRAINTS

	#what constraints must be satisfied for an interface to be restful?

		#client-server separation
		#stateless interactions
		#cacheable responses
		#uniform component interface
		#layered system
		#download code on demand




	#what does 'client-server separation' refer to?

		#separate the user interface concerns from the data storage concerns
		#this 
			#improves  portability of the user interface across multiple platforms
			#improves scalability by simplifying server components

		#A client application and server application MUST be able to evolve separately without any dependency on each other
		#A client should know only resource URIs and that’s all
		#Servers and clients may also be replaced and developed independently, as long as the interface between them is not altered.




	#what does 'stateless server storage' refer to?

		#session state is kept entirely on the client
		#no stored context on the server
		#every request must contain all the info necessary to understand the request




	#what does 'cacheable responses' refer to?

		#every response must be labeled as cacheable or non cacheable implicitly or explicitly
		#if cacheable, the client cache is given the right to reuse the data later for similar requests




	#what does 'uniform component interface' refer to?

		#principle of generality is applied to the component interface. Therefore you have:
			
			#simplified LOGICAL architecture, and
			
			#improved visibility of interactions


		#Synonymise every resource with a web page
		
		#Every resource in the system should have only one logical URI
		
		#Whenever relevant a resource should contain HATEOAS links pointing to relative URIs

			#HATEOAS means Hypermedia as the Engine of Application State

			#Hypermedia refers to any content that contains links to other forms of media

		#Once a developer becomes familiar with one of your APIs, he should be able to follow the similar approach for other APIs







	#what does 'layered system' refer to?

		#architecture is composed of hierarchical layers
		#component behaviour is constrained
		#each component cannot see beyond the immediate layer with which they are interacting




	# what does 'download code on demand' refer to?

		#REST simplifies clients by limiting the number of features needed to be pre-installed
		#you can extend client functionality by downloading and executing code in the form of applets or scripts





#RESOURCES

	#what is a resource?

		#any information that can be named

		#the key abstraction of information in REST




	#what is a resource identifier?

		#an ID used to identify the resource involved in an iteraction between components




	#what is resource representation?

		#the state of a resource at a given time
		
		#consists of
			#hypermedia links
			#data
			#metadata




	#what is a media type?

		#the DATA FORMAT of a resource representation




	#what does the media type identify?

		#a SPECIFICATION that determines HOW THE RESOURCE IS TO BE PROCESSED




	#why should a resource representation be self-descriptive?

		#because a client should be able to act on the basis of the media type associated with the resource

		#ie the client should not need to know the exact description (e.g. manager, airplane) of the resource before the client can act




	#why will you ideally need a custom media type for each resource?

		#because they will enable clients distinguish more easily one resource from the next





#RESOURCE METHODS

	#why should methods be 'uniform interface'?




	#why should methods be part of the API response for a resource?




	#why should we represent query-based API results by a list of links with summary information, and not by arrays of original resource representations? 


		#because a query is not (a substitute?) suitable for identification of resources?

		#because arrays of original resource representations are not suitable for identification of resources?







#REST RESOURCE NAMING GUIDE

	#USE NOUNS
	

	#CONSISTENCY IS THE KEY
	

	#DON'T USE CRUD FUNCTION NAMES IN URIs
		#the words post(CREATE), get(READ), put(UPDATE) and delete(DELETE) shouldn't feature in your URIs
	

	#FILTER URI COLLECTION WITH QUERY COMPONENT
		#eg 
		#http://api.arsenal.com/player-management/firstteam-players			- collection
		#http://api.arsenal.com/player-management/firstteam-players?age=31	- filtered with query component






#REST API Design Tutorial

	#Create Object Model
	#Create URIs
	#Create Representations
	#Assign HTTP Methods


	#Create Object Model

		#identify which objects will be resources
		
		#identify which objects will be subresources

		#assign a unique identifier to each resource and sub resource



	#Create URIs


	#Create Representations
		#Collection of Device Resource
		#Single Device Resource
		#Configuration Resource Collection
		#Single Configuration Resource
		#Configuration Resource Collection Under Single Device
		#Single Configuration Resource Under Single Device


	#Assign HTTP Methods
		#Browse all devices or configurations [Primary Collection]
		#Browse all devices or configurations [Secondary Collection]
		#Browse single device or configuration [Primary Collection]
		#Browse single device or configuration [Secondary Collection]
		#Create a device or configuration
		#Update a device or configuration
		#Remove a device or configuration
		#Applying or Removing a configuration from a device








#IMPLEMENTATION OF STEPS

	#CREATE OBJECT MODEL

		# collection resources

			# arsenal first team, id = 1
			# arsenal academy, id = 2
			# arsenal coaching staff, id = 3


		# singleton resources

			# petr cech, id 11
			# danny welbeck, id 12
			# unai emery, id 31
			# juan carlos carcedo, id 32


		# sub collection resources

			# matches played
			# days at work




	#CREATE URIs

	# scheme/domain/resource


		# http://api.arsenal.com/player-management/firstteam-players - collection resource
		# http://api.arsenal.com/player-management/academy-players - collection resource
		# http://api.arsenal.com/staff-management/coaching-staff - collection resource

		# http://api.arsenal.com/player-management/firstteam-players/{player-id} - singleton resource
		# http://api.arsenal.com/staff-management/coaching-staff/{staff-id} - singleton resource

		# http://api.arsenal.com/player-management/firstteam-players/{player-id}/matches-played - sub collection resource
		# http://api.arsenal.com/staff-management/coaching-staff/{staff-id}/days-at-work - sub collection resource

		# http://api.arsenal.com/player-management/firstteam-players/{player-id}/matches-played/{match-id} - singleton resource in sub collection resource
		# http://api.arsenal.com/staff-management/coaching-staff/{staff-id}/days-at-work/{date-id} - singleton resource in sub collection resource

		# http://api.arsenal.com/player-management/firstteam-players/11 - singleton resource - petr cech
		# http://api.arsenal.com/player-management/firstteam-players/12 - singleton resource - danny welbeck

		# http://api.arsenal.com/player-management/coaching-staff/31 - singleton resource - unai emery
		# http://api.arsenal.com/player-management/coaching-staff/32 - singleton resource - juan carlos carcedo






'''
	#CREATE REPRESENTATIONS

		#THE BELOW IS WRITTEN IN XML


		#REPRESENTATION FOR COLLECTION RESOURCE - FIRST TEAM PLAYERS

			<firstteam-players size="26">
			    <link rel="self" href="/firstteam-players"/>
			 

			    <firstteam-player id="11">
			    	<link rel="self" href="/firstteam-players/11"/>
			    	...
			    </firstteam-player>

			    
			    <firstteam-player id="12">
		    	    <link rel="self" href="/firstteam-players/12"/>
		    	    ...
			    </firstteam-player>


			</firstteam-players>


		#REPRESENTATION FOR SINGLETON RESOURCE - FIRST TEAM PLAYER
			
			<firstteam-player id="11">
			    <link rel="self" href="/firstteam-players/11"/>
			    ...
			 
			    <matches-played size="2">
		   		    <link rel="self" href="/matches-played"/>


				    <match-played id="567">
		   	   		    <link rel="self" href="/matches-played/567"/>
				    </match-played>

				    
				    <match-played id="789">
		   	   		    <link rel="self" href="/matches-played/789"/>
				    </match-played>

			    </matches-played>


			</firstteam-player>


		#REPRESENTATION FOR SUB COLLECTION RESOURCE - MATCHES PLAYED

			<matches-played size="38">
			    <link rel="self" href="/matches-played"/>
			 

			    <match-played id="001">
		    	    <link rel="self" href="/matches-played/001"/>
			    	...
			    </match-played>

			    
			    <match-played id="002">
		    	    <link rel="self" href="/matches-played/002"/>
			    	...
			    </match-played>


			    ...


			    ...


			</matches-played>


		#REPRESENTATION FOR SINGLETON RESOURCE IN SUB COLLECTION RESOURCE - MATCH PLAYED

		    <match-played id="001">
			    <link rel="self" href="/matches-played/001"/>
			    ...
			    <link rel="match-outcome" href="/matches-played/001/match-outcome"/>

			
			</match-played>


		#REPRESENTATION FOR SUB COLLECTION RESOURCE UNDER SINGLETON RESOURCE - MATCHES PLAYED UNDER SINGLE PLAYER

			<matches-played size="38">
			    <link rel="self" href="/firstteam-players/11/matches-played"/>
			 

			    <match-played id="001">
		    	    <link rel="self" href="/firstteam-players/11/matches-played/001"/>
		       	    <link rel="detail" href="/matches-played/001"/>
			    	...
			    </match-played>

			    
			    <match-played id="002">
			    	<link rel="self" href="/firstteam-players/11/matches-played/002"/>
		       	    <link rel="detail" href="/matches-played/002"/>
			    	...
			    </match-played>


			    ...


			    ...


			</matches-played>


		#REPRESENTATION FOR SINGLETON RESOURCE UNDER SINGLETON RESOURCE - MATCH PLAYED UNDER SINGLE PLAYER

		    <match-played id="001">
		    	<link rel="self" href="/firstteam-players/11/matches-played/001"/>
			    <link rel="detail" href="/matches-played/001"/>
			    ...
			    <link rel="match-outcome" href="/matches-played/001/match-outcome"/>

			
			</match-played>	





	#ASSIGN HTTP METHODS 		

	# what do i write (and where do i write it) to map http operations to the appropriate URIs????


		#GET
		#POST
		#PUT
		#DELETE


		# browse all firstteam-players or matches-played [Primary Collection]
		
			HTTP GET /firstteam-players
			HTTP GET /matches-played

				#apply paging and filtering

					HTTP GET /firstteam-players?startIndex=0&size=20
					HTTP GET /matches-played?startIndex=0&size=20


			# browse all matches-played [Secondary Collection]

				HTTP GET /firstteam-players/{id}/matches-played


			# browse single firstteam-player or match-played [Primary Collection]

				HTTP GET /firstteam-players/{id}
				HTTP GET /matches-played/{id}


			# browse single match-played [Secondary Collection]

				HTTP GET /firstteam-players/{id}/matches-played/{id}


		# create a firstteam-player or match-played

			HTTP POST /firstteam-players
			HTTP POST /matches-played

			# the request payload will not contain any id attribute, as the server is responsible for deciding the id(?)


		# update a firstteam-player or match-played

			HTTP PUT /firstteam-players/{id}
			HTTP PUT /matches-played/{id}


		# delete a firstteam-player or match-played

			HTTP DELETE /firstteam-players/{id}
			HTTP DELETE /matches-played/{id}
		

		# applying or removing a match played to/from a player

			# Applying

			HTTP PUT /firstteam-players/{id}/matches-played 	#no {id} specified for matches-played: should this be PUT or POST??????
 
			# Removing


			HTTP DELETE /firstteam-players/{id}/matches-played/{id} 




	#LOGGING
	#SECURITY
	#DISCOVERY
