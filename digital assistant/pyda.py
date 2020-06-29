#this application will call on the wolframalpha api and get results - from the wolframalpha website - through the wolframalpha api


#import the wikipedia api and the wolframalpha api
import wikipedia
import wolframalpha 



while True:

    #request user input
    userinput = input("Q:  ")

    #exit
    if userinput == 'exit':
        exit()

    try:#wolframalpha

        #assign my wolfram api to a variable
        app_id = "9GPURP-JKR4XYVQ8W"

        #create a client variable using the wolfram api id
        client = wolframalpha.Client(app_id)

        #create a result variable using the user input
        result = client.query(userinput)

        #convert the result to text
        answer = next(result.results).text

        #print the text 
        print (answer)


    except:#wikipedia

        #request number of sentences user wishes to see
        no_of_sentences = int(input("number of sentences: "))

        #set language
        language_input = ''
        
        language_choice = input("please select language: espanyol / francais / german / english / chinese: ")
        
        if language_choice == 'espanyol':
            language_input = "es"
        elif language_choice == 'francais':
            language_input = "fr"
        elif language_choice == 'german':
            language_input = "de"
        elif language_choice == 'english':
            language_input = "en"
        elif language_choice == 'chinese':
            language_input = "zh"
        else:
            print("\n sorry, that is not a valid language choice")
            language_input = "en"

        wikipedia.set_lang(language_input)

        #print wikipedia summary of the answer
        print("\n", wikipedia.summary(userinput, sentences=no_of_sentences))



