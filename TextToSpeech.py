'''Importing Libraries'''
from tkinter import *
import pyttsx3


'''Creating Window'''
root = Tk()
root.geometry('700x500')
root.configure(bg= 'ghost white')
root.title('Text To Speech Converter')

Label(root, text= "Text To Speech Converter", font= 'timesnewroman 20 bold', bg= 'white smoke').pack()
Label(text= 'By VKP', font= 'timesnewroman 10 italic', bg= 'white smoke').pack(side= 'bottom')


'''Function to convert text into speech'''
def tts():
    message = pyttsx3.init()
    message.say(msg.get())
    message.runAndWait()
    message.stop()
    
    
'''Function to exit'''
def Exit():
    root.destroy()
    

'''Function to reset'''
def Reset():
    msg.set("")


def savefile():
    message = pyttsx3.init()
    message.save_to_file(msg.get, 'TextToSpeech.mp3')
    message.runAndWait()
    

msg = StringVar()
Label(root, text= 'Enter Text', font= 'TimesNewRoman 15 bold', bg= 'white smoke').place(x=20, y=60)

entry_field = Entry(root, font= 'timesnewroman 15',textvariable= msg, width= '40').place(x=20, y= 100)


'''Defining Buttons'''
Button(root, text= 'Read Me', font= 'timesnewroman 10 bold', command = tts, width= '10').place(x= 40, y= 150)
Button(root, text= 'Reset', font= 'timesnewroman 10 bold', command = Reset, width= '10', bg= 'orange').place(x=180, y= 150)
Button(root, text= 'Save the file', font = 'timesnewroman 10 bold', command = savefile, width= '10', bg= 'sky blue').place(x= 320, y= 150)
Button(root, text= 'Exit', font= 'timesnewroman 10 bold', command= Exit, width= '10', bg= 'red').place(x= 450, y=150)


'''Run the program'''
root.mainloop()