# my API notes



# RESOURCES:

# 'REST API concepts and examples' (Author: 'WebConcepts' https://www.youtube.com/user/jelledTV/feed)

# 'Python and REST APIs 2 - GET Data' (Author: 'Airheads Broadcasting Channel' https://www.youtube.com/channel/UCFJCnuXFGfEbwEzfcgU_ERQ/featured)

# 'Tools for Entrepreneurs: Introduction to APIs' (Author: 'Google for Entrepreneurs' https://www.youtube.com/channel/UCkWLGZL69LhjjgGRKhcAE_w)

# 'Building a REST API in Python | Home Automation #02' (Author: 'Jake Wright' https://www.youtube.com/user/jaketvee/featured)





# WHAT IS AN API?
# WHAT IS AN API END POINT?
# MISCELLANEOUS API STUFF
# WHICH OF THE FOLLOWING ARE TRUE?
# EXAMPLES OF API CALLS
# WHAT IS THE FUNCTION OF A WEB API?
# HOW CAN YOUR APP INTERACT WITH A WEB API? GET AND POST
# WHAT WORK ENVIRONMENT DO YOU NEED FOR WORKING WITH RESTful? APIs?
# WHAT IS REST?
# WHAT IS A WEB SERVICE?
# WHY GET DATA FROM A DEVICE'S REST API (USING PYTHON)?








# WHAT IS AN API?


# part of an application that allows you to connect to that application and use it remotely


# A PROGRAM THAT ALLOWS ONE PIECE OF SOFTWARE TO TALK TO ANOTHER


# AN API IS A PROGRAM ON A SERVER THAT ALLOWS ME TO 
	
	# CONNECT MY WEB APP TO THE SERVER
	
	# REPLICATE ITS SERVICES ON MY APP?
	
	# USE ITS SERVICES FROM MY APP


# a set of definitions, protocols and tools for building software


# a set of methods of communication between software components


# a source of software building blocks 
# the building blocks are put together by a programmer


# APPLICATION - A MACHINE
# PROGRAMMING - GIVING INSTRUCTIONS
# INTERFACE - A PROGRAM THAT A MACHINE USES FOR TAKING INPUT, AND GIVING OUTPUT


# E.G. TWITTER HAS AN INTERFACE THAT HUMANS AND PROGRAMS CAN TALK TO


# an API opens an interface on it's host that i can connect to


# an API allows you create machines that talk to other machines


# why would one machine want to talk to the next?

	# so that it can use the services of the next


# the API of one machine says to another machine "this is how you talk to us"


# speaking to the API requires using specific syntax, formats


# e.g. you can write the following API request into your browser address field and click on send http://graph.facebook.com/derekdahmer?fields=first_name








# MISCELLANEOUS API STUFF


# a REST API works similarly to a website

	# - you make a call to a server 
	# - you get data back via the HTTP protocol

# there are similarities between a REST API call and loading up a web page

	# eg make an API request to Facebook's graph API
	# GET THE RESPONSE IN YOUR BROWSER
	# THE RESPONSE YOU GET IS JSON-FORMATTED DATA

# JSON javascript objject notation

	# JSON data is organised in key-value pairs
	# lightweight data-interchange format.
	# easy for humans to read and write. 
	# easy for machines to parse and generate.
	
# an API allows me to connect my app to the server of a web-based service
	
	# i code the services into my app
	# i code the API into my app
	
	# I CAN USE THE COMPANY'S SERVICES IN MY APP

	# i can use their infrastructure and bring more services to my users
	# i can boost my app's functionality

# an API opens an interface on it's host that i can connect to

# i can equally have an API on my app's back-end server

	# eg if i use a server for my content and user management

	# other apps can connect to my app via my API








# WHICH OF THE FOLLOWING ARE TRUE?

# the API makes the call?
# the API receives the call?
# the call passes through the API?
# the call uses API rules or API language?








# EXAMPLES OF REQUESTS TO APIs

# view complete response to an API request e.g. by loading up http://graph.facebook.com/derekdahmer

# view response from only selected parameters e.g. by loading up  http://graph.facebook.com/derekdahmer?fields=id,name,likes

# the parameters filter the data returned by the response

# http://maps.googleapis.com/maps/api/geocode/json?address=lagos&sensor=false

# SERVER maps.googleapis.com
# RESOURCES /maps/api/geocode/json

# the following courtesy of https://www.youtube.com/user/jelledTV/feed

# Youtube's Facebook Page via the Facebook Graph API
# http://graph.facebook.com/youtube

# Same thing, this time with filters
# https://graph.facebook.com/youtube?fields=id,likes

# Google Maps Geocode API call for the city of Chicago
# http://maps.googleapis.com/maps/api/geocode/json?address=lagos

# Apigee Instagram API console
# https://apigee.com/console/instagram








# WHAT IS THE FUNCTION OF A WEB API?


# to give out their data

# to allow your web application communicate with that data

# to allow you make new data



# A WEB API ALLOWS ME TO 

	# INTEGRATE A WEBSITE INTO MY APP?
	
	# PERFORM THE operations available on the website
	
	# USE THE SERVICES AVAILABLE ON THE WEBSITE
	
	# work with tools
	
	# perform functions
	
	# carry out actions
	


# A WEB API ALLOWS YOU TO OBTAIN ALL KINDS OF DATA FROM A WEBSITE








# HOW CAN YOUR APP INTERACT WITH A WEB API?


# GET DATA FROM AN API
# WRITE DATA TO AN API


# HTTP GET METHOD - WILL GET DATA
# HTTP POST METHOD - WILL WRITE DATA

# Best practice (WHEN WRITING DATA?) is to put the data in the body of the request

# get requests are idempotent 

	# they don't modify the contents of the database








# WHAT WORK ENVIRONMENT DO YOU NEED FOR WORKING WITH RESTful? APIs?


# AN OPERATING SYSTEM - Windows, linux or mac

# A SCRIPTING LANGUAGE? - Python

# A code editor

# A REST client eg Postman








# WHAT IS REST?


# An architectural style 

# specifies CONSTRAINTS for creating web services

	# ie specifies constraints for communicating over a network

# REpresentational State Transfer

# it is STATELESS

	# Can't store context between requests
	
		# can't remember who you are or what you've previously asked
	
	# Every request received must contain all of the information necessary to process that request








# WHAT IS A WEB SERVICE?


# A method of communication 
# between two devices 
# over a network







# WHY GET DATA FROM A DEVICE'S REST API (USING PYTHON)?

# today there is an explosion in the number of IP connected devices 

# networks are scaling ever larger

# becoming more cumbersome to manage networks using CLI commands

# easier to manage networks using code (a programmatic approach)



