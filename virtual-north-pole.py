import time

def GoodOrBad():
   global Name 
   print("Hello " + Name + ", we are checking if you've been bad or nasty")
   time.sleep(1)
   print("Uh oh, you've been bad this decade")

Name = input("Give name: ")

GoodOrBad()