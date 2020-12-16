import time
import os
import sys
import random

Basket = []
Name = ""
Credits = 0

def Menu(options, acceptableMenuChoices):
   theChoice = ""
   for option in options:
      print(option)
      print("")
   while(theChoice not in acceptableMenuChoices):
      theChoice = input("Choose ur thing idk: ").lower()
   return theChoice

def MainMenuScreen():
   os.system("cls")
   print("")
   print('''
███    ███ ███████ ███    ██ ██    ██ 
████  ████ ██      ████   ██ ██    ██ 
██ ████ ██ █████   ██ ██  ██ ██    ██ 
██  ██  ██ ██      ██  ██ ██ ██    ██ 
██      ██ ███████ ██   ████  ██████  
                                      
   ''')
   menu = Menu([
         "b - Have you been good or bad haha?", 
         "s - shop", 
         "c - credits", 
         "l - christmas song lyrics", 
         "m - meet santa", 
         "q - quit"
      ], [
         "b", 
         "s", 
         "c", 
         "l", 
         "m",
         "q"
      ])
   if menu == "b":
      GoodOrBadScreen()
   if menu == "q":
      GoodByeScreen()
   if menu == "s":
      ShopScreen()
   if menu == "c":
      CreditsScreen()
   if menu == "l":
      LyricsScreen()
   if menu == "m":
      MeetSantaScreen()

def GenerateSnowLine():
   SnowLine = []
   Snow = []
   for i in range(0, 3):
      Snow.append(random.randint(0, 70))
   for i in range(0, 70):
      if i in Snow: 
         SnowLine.append("❆")
      else:
         SnowLine.append(" ")
   print("".join(SnowLine))

def LoadingScreen():
   os.system("cls")
   print("Loading...")
   for i in range(0, 15):
      time.sleep(0.2)
      GenerateSnowLine()
   time.sleep(1)

def GetNumberFromUser(message, errormessage):
   ValidInputGiven = False
   while ValidInputGiven == False:
      stringInput = input(message)
      if stringInput.isdigit() == False:
         print(errormessage)
      else:
         ValidInputGiven = True
   integer = int(stringInput)
   return integer

def ShopScreen():
   global Credits
   global Name
   os.system("cls")
   print('''
███████ ██   ██  ██████  ██████  
██      ██   ██ ██    ██ ██   ██ 
███████ ███████ ██    ██ ██████  
     ██ ██   ██ ██    ██ ██      
███████ ██   ██  ██████  ██      
   ''')
   print("Welcome to ye olde Shoppe " + Name)
   time.sleep(0.5)
   print("You have " + str(Credits) + " credits")
   print("")
   ShopMenu = Menu([
      "a - add credits to your account",
      "b - browse ye olde shoppe",
      "c - checkout",
      "q - quit to main menu"
   ], [
      "a",
      "b",
      "c",
      "q"
   ])
   if ShopMenu == "a":
      AddCredits = GetNumberFromUser("How many credits do you want to add?: ", "It's a number not rocket science")
      Credits = Credits + AddCredits
      print("Added " + str(AddCredits) + " to your account")
      time.sleep(1)
      ShopScreen()
   if ShopMenu == "q":
      MainMenuScreen()
   if ShopMenu == "b":
      BrowseShopScreen()
   if ShopMenu == "c":
      CheckoutScreen()

def CheckoutScreen():
   global Credits
   global Basket
   os.system("cls")
   print("In your basket there is: ")
   print("")
   for item in Basket:
      print("- " + item)
   print("")
   ShopMenu = Menu([
      "b - buy now",
      "t - buy more things",
      "q - quit to shop"
   ], [
      "b",
      "t",
      "q"
   ])
   if ShopMenu == "b":
      print("sorting out now calm down")
      Basket = []
      time.sleep(3)
      print("sent :)")
      time.sleep(1)
      MainMenuScreen()
   if ShopMenu == "t":
      print("okey dokey")
      time.sleep(1)
      BrowseShopScreen()
   if ShopMenu == "q":
      ShopScreen()

def BrowseShopScreen():
   os.system("cls")
   global Credits
   global Basket
   print("Welkomm to ye olde shoppe shop")
   print("You have " + str(Credits) + " to spend")
   ShopOptions = Menu([
      "1 - Santa (500 credits)",
      "2 - reindeer (50 credits)",
      "3 - The north pole (500000 credits)",
      "4 - santa klaus suit - (5 credits)",
      "5 - elf (500 credits)",
      "q - quit to main shop menu (or checkout)"
   ], [
      "1",
      "2",
      "3",
      "4",
      "5",
      "q"
   ])
   if ShopOptions == "1":
      AddToBasket(500, "SANTA")
      time.sleep(1)
      BrowseShopScreen()
   if ShopOptions == "2":
      AddToBasket(50, "REINDEER")
      time.sleep(1)
      BrowseShopScreen()
   if ShopOptions == "3":
      AddToBasket(500000, "NORTH POLE")
      time.sleep(1)
      BrowseShopScreen()
   if ShopOptions == "4":
      AddToBasket(5, "SUIT")
      time.sleep(1)
      BrowseShopScreen()
   if ShopOptions == "5":
      AddToBasket(500, "ELF")
      time.sleep(1)
      BrowseShopScreen()
   if ShopOptions == "q":
      ShopScreen()

def AddToBasket(cost, title):
   global Credits
   if Credits < cost:
      print("Not enough moneys to buy this thing or person it depends")
   else:
      Credits = Credits - cost
      Basket.append(title)
      print("added " + title + " to your basket")

def CreditsScreen():
   os.system("cls")
   print("******************************************")
   CharacterTyping("It was me all along mwahahahahahaha")
   print("******************************************")
   time.sleep(1)
   print("jk jk lol")
   time.sleep(1)
   print("")
   print("******************************************")
   print("")
   CharacterTyping("code - by me")
   print("")
   time.sleep(1)
   CharacterTyping("ascii pictures - mr google")
   print("")
   time.sleep(1)
   CharacterTyping("awful jokes - dad")
   print("")
   print("******************************************")
   time.sleep(2)
   MainMenuScreen()

def LyricsScreen():
   os.system("cls")
   print("Choose your Christmas song lyrics yay: ")
   print("")
   ChooseSong = Menu([
      "1 - Deck The Halls",
      "2 - Jingle Bells",
      "3 - Joy to the World",
      "q - quit to main menu"
   ], [
      "1",
      "2",
      "3",
      "q"
   ])
   if ChooseSong == "1":
      os.system("cls")
      CharacterTyping('''
Deck the halls with boughs of holly, Fa la la la la la la la!

'Tis the season to be jolly, Fa la la la la la la la!
Don we now our gay apparel, Fa la la la la la la la!
Troll the ancient Yuletide carol, Fa la la la la la la la!

See the blazing yule before us, Fa la la la la la la la!
Strike the harp and join the chorus, Fa la la la la la la la!

Follow me in merry measure, Fa la la la la la la la!
While I tell of Yuletide treasure, Fa la la la la la la la!

Fast away the old year passes, Fa la la la la la la la!
Hail the new, ye lads and lasses, Fa la la la la la la la!
Sing we joyous all together! Fa la la la la la la la!
Heedless of the wind and weather, Fa la la la la la la la!
      ''', 300)
      input("Press ENTER to choose another song or quit: ")
      LyricsScreen()

   if ChooseSong == "2":
      os.system("cls")
      CharacterTyping('''
Dashing through the snow
On a one horse open sleigh
O'er the fields we go,
Laughing all the way
Bells on bob tail ring,
making spirits bright
What fun it is to laugh and sing
A sleighing song tonight

Oh, jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh
Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh
      ''', 300)
      input("Press ENTER to choose another song or quit: ")
      LyricsScreen()

   if ChooseSong == "3":
      os.system("cls")
      CharacterTyping('''
Joy to The world! the Lord is come
Let earth receive her King
Let ev'ry heart prepare him room
And heaven and nature sing
And heaven and nature sing
And heaven and nature sing

Joy to the world! the Savior reigns
Let men their songs employ
While fields and floods, rocks, hills and plains
Repeat the sounding joy
Repeat the sounding joy
Repeat the sounding joy

No more let sins and sorrows grow,
Nor thorns infest the ground;
He comes to make His blessings flow
Far as the curse is found,
Far as the curse is found,
Far as, far as, the curse is found.

He rules the world with truth and grace
And makes the nations prove
The glories of His righteousness
And wonders of His love
And wonders of His love
And wonder wonders of His love
      ''', 300)
      input("Press ENTER to choose another song or quit: ")
      LyricsScreen()

   if ChooseSong == "q":
      MainMenuScreen()

def MeetSantaScreen():
   os.system("cls")
   PrintPicture('''
                              ..,,,,,,,,,,,,,,,,.. 
                        ..,,;;;;;;;;;;;;;;;;;;;;;;;;;;,,. 
                    .,::::;;;;aaaaaaaaaaaaaaaaaaaaaaaaaaa;;,,. 
                .,;;,:::a@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@a, 
              ,;;;;.,a@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@a 
           ,;;;;%;.,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@a, 
        ,;%;;;;%%;,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ 
     ,;;%%;;;;;%%;;@@@@@@@@@@@@@@'%v%v%v%v%v%v%v%v%v%v%v%v`@@@@@@@@@ 
   ,;;%%;;;;:;;;%;;@@@@@@@@@'%vvvvvvvvvnnnnnnnnnnnnnnnnvvvvvv%`@@@@' 
  ,;%%;;;;;:;;;;;;;;@@@@@'%vvva@@@@@@@@avvnnnnnnnnnnvva@@@@@@@OOov, 
 ,;%;;;;;;:::;;;;;;;@@'OO%vva@@@@@@@@@@@@vvnnnnnnnnvv@@@@@@@@@@@Oov 
 ;%;;;;;;;:::;;;;;;;;'oO%vvn@@%nvvvvvvvv%nnnnnnnnnnnnn%vvvvvvnn%@Ov 
 ;;;;;;;;;:::;;;;;;::;oO%vvnnnn>>nn.   `nnnnnnnnnnnn>>nn.   `nnnvv' 
 ;;;;;;;;;:::;;;;;;::;oO%vvnnvvmmmmmmmmmmvvvnnnnnn;%mmmmmmmmmmmmvv, 
 ;;;;;;;;;:::;;;;;;::;oO%vvmmmmmmmmmmmmmmmmmvvnnnv;%mmmmmmmmmmmmmmmv, 
 ;;;;;;;;;;:;;;;;;::;;oO%vmmmmnnnnnnnnnnnnmmvvnnnvmm;%vvnnnnnnnnnmmmv 
  `;%;;;;;;;:;;;;::;;o@@%vvmmnnnnnnnnnnnvnnnnnnnnnnmmm;%vvvnnnnnnmmmv 
   `;;%%;;;;;:;;;::;.oO@@%vmmnnnnnnnnnvv%;nnnnnnnnnmmm;%vvvnnnnnnmmv' 
     `;;;%%;;;:;;;::;.o@@%vvnnnnnnnnnnnvv%;nnnnnnnmm;%vvvnnnnnnnv%'@a. 
      a`;;;%%;;:;;;::;.o@@%vvvvvvvvvvvvvaa@@@@@@@@@@@@aa%%vvvvv%%@@@@o. 
     .@@o`;;;%;;;;;;::;,o@@@%vvvvvvva@@@@@@@@@@@@@@@@@@@@@avvvva@@@@@%O, 
    .@@@@@Oo`;;;;;;;;::;o@@@@@@@@@@@@@@@@@@@@"""""""@@@@@@@@@@@@@@@@@OO@a 
  .@@@@@@@@@OOo`;;;;;;:;o@@@@@@@@@@@@@@@@"           "@@@@@@@@@@@@@@oOO@@@, 
 .@@@@o@@@@@@@OOo`;;;;:;o,@@@@@@@@@@%vvvvvvvvvvvvvvvvvv%%@@@@@@@@@oOOO@@@@@, 
 @@@@o@@@@@@@@@OOo;::;'oOOooooooooOOOo%vvvvvvvvvvvvvv%oOOooooooooOOO@@@O@@@, 
 @@@oO@@@@@@@@@OOa@@@@@a,oOOOOOOOOOOOOOOoooooooooooooOOOOOOOOOOOOOO@@@@Oo@@@ 
 @@@oO@@@@@@@OOa@@@@@@@@Oo,oO@@@@@@@@@@OOOOOOOOOOOOOO@@@@@@@@@@@@@@@@@@Oo@@@ 
 @@@oO@@@@@@OO@@@@@@@@@@@OO,oO@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@Oo@@@ 
 @@@@o@@@@@@OO@@@@@@@@@@OOO,oO@@@@@@@@@O@@@@@@@@@@@@@@@@@@@@@o@@@@@@@@@O@@@@ 
 @@@@@o@@@@@OOo@@@@@@@OOOO'oOO@@@@@@@@Oo@@@@@@@@@@@@O@@@@@@@@Oo@@@@@@@@@@@@a 
`@@@@@@@O@@@OOOo`OOOOOOO'oOO@@@@@@@@@O@@@@@@@@@@@@@@@O@@@@@@@@Oo@@@@@@@@@@@@ 
 `@@@@@OO@@@@@OOOooooooooOO@@@@@@@@@@@@@@@@@@@@@@@@@@Oo@@@@@@@Oo@@@@@@oO@@@@ 
   `@@@OO@@@@@@@@@@@@@@@@@@@O@@@@@@@@@@@@@@@@@@@@@@@@Oo@@@@@@@O@@@@@@@oO@@@' 
      `@@`O@@@@@@@@@@@@@@@@@@@Oo@@@@@@@@@@@@@@@@@@@@@@Oo@@@@@@@@@@@@@@@O@@@' 
        `@ @@@@@@@@@@@@@@@@@@@OOo@@@@@@@@@@@@@@@@@@@@@O@@@@@@@@@@@@@@@'@@' 
           `@@@@@@@@@@@@@@@@@@OOo@@@@@@@@@@@@@@@@@@@@O@@@@@@@@@@@@@@@ a' 
               `@@@@@@@@@@@@@@OOo@@@@@@@@@@@@@@@@@@@@@@@@Oo@@@@@@@@' 
                  `@@@@@@@@@@@Oo@@@@@@@@@@@@@@@@@@@@@@@@@Oo@@@@' 
                      `@@@@@@Oo@@@@O@@@@@@@@@@@@@@@@@@@'o@@' 
                          `@@@@@@@@oO@@@@@@@@@@@@@@@@@ a' 
                              `@@@@@oO@@@@@@@@@@@@@@' ' 
                                '@@@o'`@@@@@@@@' 
                                 @'   .@@@@' 
                                     @@' 
                                   @'
''')
   time.sleep(0.5)
   CharacterTyping("I see you " + Name + "...", 30)
   print("")
   print("Questions to ask him (enter corresponding number): ")
   MeetSantaMenu()

def MeetSantaMenu():
   print("")
   SantaMenu = Menu([
      "1 - Why did you choose this job?", 
      "2 - Do the reindeer smell really bad when you are on your sleigh?",
      "3 - Is the beard real?",
      "q - quit to main menu"
   ], [
      "1",
      "2",
      "3",
      "q"
   ])
   if SantaMenu == "1":
      os.system("cls")
      print("Why did you choose this job?")
      CharacterTyping("Mid life crisis -_-", 40)
      input("Press ENTER to ask another question or quit: ")
      MeetSantaMenu()
   if SantaMenu == "2":
      os.system("cls")
      print("Do the reindeer smell really bad when you are on your sleigh?")
      CharacterTyping("My gas mask helps a lot with it, but yes", 40)
      input("Press ENTER to ask another question or quit: ")
      MeetSantaMenu()
   if SantaMenu == "3":
      os.system("cls")
      print("Is the beard real?")
      CharacterTyping("very much so, and I know it's gorgeous no need to fuss", 40)
      input("Press ENTER to ask another question or quit: ")
      MeetSantaMenu()
   if SantaMenu == "q":
      MainMenuScreen()

def WelcomeScreen():
   os.system("cls")
   global Name
   print('''
███    ██  ██████  ██████  ████████ ██   ██     ██████   ██████  ██      ███████ 
████   ██ ██    ██ ██   ██    ██    ██   ██     ██   ██ ██    ██ ██      ██      
██ ██  ██ ██    ██ ██████     ██    ███████     ██████  ██    ██ ██      █████   
██  ██ ██ ██    ██ ██   ██    ██    ██   ██     ██      ██    ██ ██      ██      
██   ████  ██████  ██   ██    ██    ██   ██     ██       ██████  ███████ ███████ 
   ''')
   PrintPicture('''
             .     .  .      +     .      .          .
     .       .      .     #       .           .
        .      .         ###            .      .      .
      .      .   "#:. .:##"##:. .:#"  .      .
          .      . "####"###"####"  .
       .     "#:.    .:#"###"#:.    .:#"  .        .       .
  .             "#########"#########"        .        .
        .    "#:.  "####"###"####"  .:#"   .       .
     .     .  "#######""##"##""#######"                  .
                ."##"#####"#####"##"           .      .
    .   "#:. ...  .:##"###"###"##:.  ... .:#"     .
      .     "#######"##"#####"##"#######"      .     .
    .    .     "#####""#######""#####"    .      .
            .     "      000      "    .     .
       .         .   .   000     .        .       .
.. .. ..................O000O........................ ...... ...
   ''')
   Name = input("Give name: ")
   if Name.upper() == "REUBEN":
      print("Welkomm master")

def CharacterTyping(message, speed = 50):
   for l in message:
      sys.stdout.write(l)
      sys.stdout.flush()
      time.sleep(random.random()*10.0/speed)
   print("")

def PrintPicture(picture, speed = 0.05):
   lines = picture.splitlines()
   for line in lines:
      print(line)
      time.sleep(speed)

def GoodOrBadScreen():
   global Credits
   os.system("cls")
   global Name
   print("Hello " + Name + ", we are checking if you've been bad or nasty")
   time.sleep(1)
   print("boop beep bop...")
   time.sleep(1)
   if Name.upper() == "REUBEN":
      print("hacks lol")
      time.sleep(0.5)
      print("*added 10000000000 credits*")
      Credits = Credits + 10000000000
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
