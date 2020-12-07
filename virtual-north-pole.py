import time

def Menu(options, acceptableMenuChoices):
   theChoice = ""
   while(theChoice not in acceptableMenuChoices):
      for option in options:
         print(option)
      theChoice = input("Choose ur thing idk: ").lower()
   return theChoice

def MainMenuScreen():
   menu = Menu(["1 - Have you been good or bad haha?", "q - quit"], ["1", "q"])
   if menu == "1":
      GoodOrBadScreen()
   if menu == "q":
      GoodByeScreen()
      
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

WelcomeScreen()
MainMenuScreen()