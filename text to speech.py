import pyttsx3
x=pyttsx3.init()
a=input("Enter the text you want to convert into speech")
x.save_to_file(a,"python.mp3")
x.runAndWait()

