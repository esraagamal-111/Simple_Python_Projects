print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction = (input('Would you like to go Left or Right? ')).lower()

if direction == 'left':
    swim = (input('Would you like to go Swim or Wait? ')).lower()

    if swim == 'wait':
        door = (input(""" Which door would you like to open

                              ______
                           ,-' ;  ! `-.
                          / :  !  :  . \
                         |_ ;   __:  ;  |
                         )| .  :)(.  !  |
                         |"    (##)  _  |
                         |  :  ;`'  (_) (
                         |  :  :  .     |
                         )_ !  ,  ;  ;  |
                         || .  .  :  :  |
                         |" .  |  :  .  |
                         |mt-2_;----.___|  
                                Blue
                              ________
                             / ______ \
                             || _  _ ||
                             ||| || |||
                             |||_||_|||
                             || _  _o|| (o)
                             ||| || |||
                             |||_||_|||      ^~^  ,
                             ||______||     ('Y') )
                            /__________\    /   \/
                    ________|__________|__ (\|||/) _________
                           /____________\
                           |____________|    
                                Red
                            __________
                           |  __  __  |
                           | |  ||  | |
                           | |  ||  | |
                           | |__||__| |
                           |  __  __()|
                           | |  ||  | |
                           | |  ||  | |
                           | |  ||  | |
                           | |  ||  | |
                           | |__||__| |
                           |__________|    
                              Yellow

                     (Blue, Red, Yellow )? 


                     """)).lower()

        if door == 'blue':
            print("""
                    Eaten by Beast
                               (    )
                              ((((()))
                              |o\ /o)|
                              ( (  _')
                               (._.  /\__
                              ,\___,/ '  ')
                '.,_,,       (  .- .   .    )
                 \   \\     ( '        )(    )
                  \   \\    \.  _.__ ____( .  |
                   \  /\\   .(   .'  /\  '.  )
                    \(  \\.-' ( /    \/    \)
                     '  ()) _'.-|/\/\/\/\/\|
                         '\\ .( |\/\/\/\/\/|
                           '((  \    /\    /
                           ((((  '.__\/__.')
                            ((,) /   ((()   )
                             "..-,  (()("   /
                              _//.   ((() ."
                      _____ //,/" ___ ((( ', ___
                                       ((  )
                                        / /
                                      _/,/'
                                    /,/,"

                  Game Over :( 
            """)
        elif door == 'red':
            print('''
                -=[ Burned by Fire ]=-  

                                                               )
                  ,%,                                     ) _(___[]_
                  %%%,&&&,                     ,%%,      (;`       /\
                  %Y/%&&&&                     %%%%   ___/_____)__/ _\__     ,%%,
                ^^^||^&\Y&^^^^^^^^^^^^^^^^^^^^^%Y/%^^/ (_()   (  | /____/\^^^%%%%^^
                  `    || _,..=xxxxxxxxxxxx,    ||   |(' |LI (.)I| | LI ||   %\Y%
                 -=      /L_Y.-"""""""""`,-n-. `    @'---|__||___|_|____||_   ||
                ___-=___.--'[========]|L]J: []\ __________@//@___________) )______
               -= _ _ _ |/ _ ''_ " " ||[ -_ 4 |  _  _  _  _  _  _  _  _  _  _  _
                        '-(_)-(_)----'v'-(_)--'
               ------------------------------------------------------------------

                     Game Over :(
                    ''')
        elif door == 'yellow':
            print('''
            Congratulations; 
            *******************************************************************************
                      |                   |                  |                     |
             _________|________________.=""_;=.______________|_____________________|_______
            |                   |  ,-"_,=""     `"=.|                  |
            |___________________|__"=._o`"-._        `"=.______________|___________________
                      |                `"=._o`"=._      _`"=._                     |
             _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
            |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
            |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
                      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
             _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
            |                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
            |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
            ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
            /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
            ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
            /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
            ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
            /______/______/______/______/______/______/______/______/______/______/_____ /
            *******************************************************************************
                   You Won! :)
            ''')
        else:
            print('''
                attacked by Lion


                                                        ,w.
                                                      ,YWMMw  ,M  ,
                                 _.---.._   __..---._.'MMMMMw,wMWmW,
                            _.-""        """           YP"WMMMMMMMMMb,
                         .-' __.'                   .'     MMMMW^WMMMM;
             _,        .'.-'"; `,       /`     .--""      :MMM[==MWMW^;
          ,mM^"     ,-'.'   /   ;      ;      /   ,       MMMMb_wMW"  @\
         ,MM:.    .'.-'   .'     ;     `\    ;     `,     MMMMMMMW `"=./`-,
         WMMm__,-'.'     /      _.\      F"""-+,,   ;_,_.dMMMMMMMM[,_ / `=_}
         "^MP__.-'    ,-' _.--""   `-,   ;       \  ; ;MMMMMMMMMMW^``; __|
                    /   .'            ; ;         )  )`{  \ `"^W^`,   \  :
                   /  .'             /  (       .'  /     Ww._     `.  `"
                  /  Y,              `,  `-,=,_{   ;      MMMP`""-,  `-._.-,
         fsc     (--, )                `,_ / `) \/"")      ^"      `-, -;"\:
                  `"""                    `"""   `"'                  `---" 

            Game Over :(
            ''')

    else:
        print("""
                Attacked by Crocodile 

                       _.---._     .---.
                __...---' .---. `---'-.   `.
      ~ -~ -.-''__.--' _.'( | )`.  `.  `._ :
     -.~~ .'__-'_ .--'' ._`---'_.-.  `.   `-`.
      ~ ~_~-~-~_ ~ -._ -._``---. -.    `-._   `.
        ~- ~ ~ -_ -~ ~ -.._ _ _ _ ..-_ `.  `-._``--.._
         ~~-~ ~-_ _~ ~-~ ~ -~ _~~_-~ -._  `-.  -. `-._``--.._.--''. ~ -~_
             ~~ -~_-~ _~- _~~ _~-_~ ~-_~~ ~-.___    -._  `-.__   `. `. ~ -_~
                 ~~ _~- ~~- -_~  ~- ~ - _~~- _~~ ~---...__ _    ._ .` `. ~-_~
                    ~ ~- _~~- _-_~ ~-_ ~-~ ~_-~ _~- ~_~-_~  ~--.....--~ -~_ ~
                         ~ ~ - ~  ~ ~~ - ~~-  ~~- ~-  ~ -~ ~ ~ -~~-  ~- ~-~ 

            Game Over :(  
            """)



else:
    print(""" Fall into a hole 
                                888             888         
                            888             888         
                            888             888         
                            88888b.  .d88b. 888 .d88b.  
                            888 "88bd88""88b888d8P  Y8b 
                            888  888888  88888888888888 
                            888  888Y88..88P888Y8b.     
                            888  888 "Y88P" 888 "Y8888  
           
           :(, Game Over
        """)

