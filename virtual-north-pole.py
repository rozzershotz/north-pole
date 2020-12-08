import time

def Menu(options, acceptableMenuChoices):
   theChoice = ""
   while(theChoice not in acceptableMenuChoices):
      for option in options:
         print(option)
      theChoice = input("Choose ur thing idk: ").lower()
   return theChoice

def MainMenuScreen():
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
   print("Loading...")
   time.sleep(1)

def ShopScreen():
   print("ShopScreen")

def RandomPictureScreen():
   print("RandomPictureScreen")

def CreditsScreen():
   print("CreditsScreen")

def LyricsScreen():
   print("LyricsScreen")

def MeetSantaScreen():
   print("MeetSantaScreen")

def WelcomeScreen():
   global Name
   print("Welcome to Santa")
   Name = input("Give name: ")

def GoodOrBadScreen():
   global Name
   print("Hello " + Name + ", we are checking if you've been bad or nasty")
   time.sleep(1)
   print("Uh oh, you've been bad this decade")

def GoodByeScreen():
   print('''
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
   print("okey bye")

LoadingScreen()
WelcomeScreen()
MainMenuScreen()