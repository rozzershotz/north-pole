import time


def Menu(options, acceptableMenuChoices):
   theChoice = ""
   while(theChoice not in acceptableMenuChoices):
   
      for option in options:
         print(option)

      theChoice = input("Choose ur thing idk: ").upper()
   
   return theChoice

def GoodOrBad():
   global Name
   print("Hello " + Name + ", we are checking if you've been bad or nasty")
   time.sleep(1)
   print("Uh oh, you've been bad this decade")

Name = input("Give name: ")

menu = Menu(["1 - option1", "2 - option2", "3 - option3", "q - quit"], ["1", "2", "3","q"])

GoodOrBad()
