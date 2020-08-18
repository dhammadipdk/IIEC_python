import os

import pyttsx3

print("\n")

print("Hello, I am Dhammadip Kamble.")

print("\n")

pyttsx3.speak("hello. i am  dhammadip kamblay")

#if opened using notepad, my name spell is "dhammadip kamble"

print("Welcome to this basic operation where I am your Assistant.")

pyttsx3.speak("Welcome to this basic operation where I am your Assistant.")

print("I will help you to open desired application in your Computer.")

pyttsx3.speak("I will help you to open desired application in your Computer.")

while True:
  
  print("\n")

  print("Chat with your Requirements: " , end='')

  p=input()
 
  if (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("chrome" in p) or ("browser" in p)):
    os.system("chrome")

  elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("notepad" in p) or ("text editor" in p)):
    os.system("notepad")

  elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("windows media player" in p) or ("wmplayer" in p)):
    os.system("wmplayer")

  elif ("exit" in p) or ("stop" in p) or ("quit" in p) or ("end" in p):
    break

  elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("calci" in p) or ("calc" in p) or ("calcy" in p) or ("calculator" in p)):
    os.system("calc")

  elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("paint" in p) or ("mspaint" in p)):
    os.system("mspaint")

  elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("vlc" in p) or ("vlc media player" in p)):
    os.system("vlc")

  elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and ("internet explorer" in p):
    os.system("iexplore")

  elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("access" in p) or ("msaccess" in p)):
    os.system("msaccess")

  elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("powerpoint" in p) or ("mspowerpoint" in p)):
    os.system("powerpnt")
 
  elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("word" in p) or ("msword" in p)):
    os.system("winword")

  elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("outlook" in p) or ("msoutlook" in p)):
    os.system("outlook")
 
  elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("excel" in p) or ("msexcel" in p)):
    os.system("excel")
 
  elif (("run" in p) or ("launch" in p) or ("open" in p) or ("execute" in p)) and (("onenote" in p) or ("msonenote" in p)): 
    os.system("onenote")

  else:
    print("Invalid Input.")

print("\n")

print("Thank You.")

pyttsx3.speak("thank you") 