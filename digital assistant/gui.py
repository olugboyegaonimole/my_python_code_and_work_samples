#from espeak import espeak
import wx
import wikipedia
import wolframalpha
import subprocess

import speake3

#C:\Program Files\Git\usr\binC:\Program Files\Git\usr\bin

engine = speake3.Speake() # Initialize the speake engine
engine.set('voices', 'en')
engine.set('speed', '107')
engine.set('pitch', '99')
engine.say("Hello world!") #String to be spoken
engine.talkback()



class OlusFrame(wx.Frame):

    def espeak(text: str, pitch: int=50) -> int:
        """ Use espeak to convert text to speech. """
        return subprocess.run(['espeak', f'-p {pitch}', text]).returncode


    def __init__(self):
        wx.Frame.__init__(
            self, 
            None,
            pos = wx.DefaultPosition,
            size = wx.Size(450, 100),
            style = wx.MINIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION | wx.CLOSE_BOX | wx.CLIP_CHILDREN,
            title = "Gabby Sam David"
            )
        
        panel = wx.Panel(self)
        my_sizer = wx.BoxSizer(wx.VERTICAL)
        lbl = wx.StaticText (panel, label="Hello Gabby Sam David! I am your digital assistant! How can i help you today!")

        my_sizer.Add(lbl, 0, wx.ALL, 5)
        self.txt = wx.TextCtrl(panel, style=wx.TE_PROCESS_ENTER, size=(400,30))
        self.txt.SetFocus()
        self.txt.Bind(wx.EVT_TEXT_ENTER, self.OnEnter)
        my_sizer.Add(self.txt, 0, wx.ALL, 5)
        panel.SetSizer(my_sizer)
        self.Show()

    def OnEnter(self, event):
        userinput = self.txt.GetValue()
        userinput = userinput.lower()

        if "who is " in userinput:
            userinput = userinput.strip("who is ")


        #print("it worked")
        
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
            global answer 
            answer = next(result.results).text

            #print the text 
            print(answer)

            #speak the answer



        except:#wikipedia
            """

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

            """

            #convert user input to a list
            userinput = userinput.split(" ")
            
            #define stop words
            #stopwords = ["and", "or", "never", "not", "what", "why", "how", "many", "are", "the", "a", "was", "were", "did", "which", "will", "be", "would", "could", "should", "can", "shall", "is", "when", "where", "who"]
            stopwords = ["and", "or", "never", "not", "what", "why", "how", "many", "are", "the", "a", "was", "were", "did", "which", "will", "be", "would", "could", "should", "can", "shall", "is"]

            #remove stop words from user input list
            userinput = [i for i in userinput if i not in stopwords]

            #convert user input to string
            userinput = " ".join(userinput)
            

            #print wikipedia summary of the answer
            #print("\n", wikipedia.summary(userinput))


if __name__ == "__main__":
    app = wx.App(True)
    frame = OlusFrame()
    app.MainLoop()
