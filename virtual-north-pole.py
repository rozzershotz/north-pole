import time
import os

def Menu(options, acceptableMenuChoices):
   theChoice = ""
   while(theChoice not in acceptableMenuChoices):
      for option in options:
         print(option)
      theChoice = input("Choose ur thing idk: ").lower()
   return theChoice

def MainMenuScreen():
   os.system("cls")
   print("")
   menu = Menu(["b - Have you been good or bad haha?", "s - shop", "r - random christmas picture", "c - credits", "l - christmas song lyrics", "m - meet santa", "q - quit"], ["b", "s", "r", "c", "l", "m","q"])
   if menu == "b":
      GoodOrBadScreen()
   if menu == "q":
      GoodByeScreen()
   if menu == "s":
      ShopScreen()
   if menu == "r":
      RandomPictureScreen()
   if menu == "c":
      CreditsScreen()
   if menu == "l":
      LyricsScreen()
   if menu == "m":
      MeetSantaScreen()

def LoadingScreen():
   os.system("cls")
   print("Loading...")
   time.sleep(1)

def ShopScreen():
   os.system("cls")
   print("ShopScreen")

def RandomPictureScreen():
   os.system("cls")
   print("RandomPictureScreen")

def CreditsScreen():
   os.system("cls")
   print("CreditsScreen")

def LyricsScreen():
   os.system("cls")
   print("LyricsScreen")

def MeetSantaScreen():
   os.system("cls")
   print("MeetSantaScreen")

def WelcomeScreen():
   os.system("cls")
   global Name
   print("Welcome to Santa")
   Name = input("Give name: ")
   if Name.upper() == "REUBEN":
      print("Welkomm master")

def PrintPicture(picture):
   lines = picture.splitlines()
   for line in lines:
      print(line)
      time.sleep(0.05)

def GoodOrBadScreen():
   os.system("cls")
   global Name
   print("Hello " + Name + ", we are checking if you've been bad or nasty")
   time.sleep(1)
   print("boop beep bop...")
   time.sleep(1)
   if Name.upper() == "REUBEN":
      print("no comment.")
   else:
      print("Uh oh, you've been bad this decade hahahahahhahhahahadahdahhfwrehbgiurefaya")
   input("press ENTER to go back to main menyu: ")
   MainMenuScreen()

def GoodByeScreen():
   os.system("cls")
   PrintPicture('''
    |,\/,| |[_' |[_]) |[_]) \\//
    ||\/|| |[_, ||'\, ||'\,  ||
            ___ __ __ ____  __  __  ____  _  _    __    __
           // ' |[_]| |[_]) || ((_' '||' |,\/,|  //\\  ((_'
           \\_, |[']| ||'\, || ,_))  ||  ||\/|| //``\\ ,_))
                                                               
                                         ,;7,
                                       _ ||:|,
                     _,---,_           )\'  '|
                   .'_.-.,_ '.         ',')  j
                  /,'   ___}  \        _/   /
      .,         ,1  .''  =\ _.''.   ,`';_ |
    .'  \        (.'T ~, (' ) ',.'  /     ';',
    \   .\(\O/)_. \ (    _Z-'`>--, .'',      ;
     \  |   I  _|._>;--'`,-j-'    ;    ',  .'
    __\_|   _.'.-7 ) `'-' "       (      ;'
  .'.'_.'|.' .'   \ ',_           .'\   /
  | |  |.'  /      \   \          l  \ /
  | _.-'   /        '. ('._   _ ,.'   \i
,--' ---' / k  _.-,.-|__L, '-' ' ()    ;
 '._     (   ';   (    _-}             |
  / '     \   ;    ',.__;         ()   /
 /         |   ;    ; ___._._____.: :-j
|           \,__',-' ____: :_____.: :-\\
|               F :   .  ' '        ,  L
',             J  |   ;             j  |
  \            |  |    L            |  J
   ;         .-F  |    ;           J    L
    \___,---' J'--:    j,---,___   |_   |
              |   |'--' L       '--| '-'|
               '.,L     |----.__   j.__.'
                | '----'   |,   '-'  }
                j         / ('-----';
               { "---'--;'  }       |
               |        |   '.----,.'
               ',.__.__.'    |=, _/
                |     /      |    '.
                |'= -x       L___   '--,
                L   __\          '-----'
                 '.____)

   ''')
   time.sleep(0.5)
   print("okey bye")

LoadingScreen()
WelcomeScreen()
MainMenuScreen()