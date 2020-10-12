import os
from PIL import ImageFont, Image, ImageDraw
class MenuOptions:


    def showTextAscii(self, message):
        ShowText = message
        #version = 'v. 1.0.0.1'

        font = ImageFont.truetype('arialbd.ttf', 15) #load the font
        size = font.getsize(ShowText)  #calc the size of text in pixels
        image = Image.new('1', size, 1)  #create a b/w image
        draw = ImageDraw.Draw(image)
        draw.text((0, 0), ShowText, font=font) #render the text to the bitmap
        for rownum in range(size[1]): 
            line = []
            for colnum in range(size[0]):
                if image.getpixel((colnum, rownum)): 
                    line.append(' '),
                else: 
                    line.append('#'),
            print (''.join(line))

        
    def getBrowserDetails(self):
            isCorect = True
            while isCorect:
                try: 
                    browserIndex = int(input('Browserul Folosit: \n' 
                    '1 - Google Chrome \n'
                    '2 - Mozilla Firefox\n'))   
                    
                    if browserIndex == 1:
                        isCorect = False
                    elif browserIndex == 2:
                        isCorect = False

                except ValueError:
                    print('Optiunea selectata nu exista')
                    
            return browserIndex





    def checkAndReturnLimitInput(self):
        # prima data se selecteaza limita cati urmaritori vrei pentru fiecare user din lista
        isOkOptionLimit = True
        while isOkOptionLimit:
            try:
                limitInput = int(input('Limita de urmaritori accesati pentru fiecare utilizator , 0 - Exit \n'))  
                if limitInput == 0:
                    exit
                isOkOptionLimit = False    
            except ValueError:
                print('Optiunea selectata nu este valida!')

        return limitInput
    
    def checkAndReturnLimitLikePosts(self):
        # prima data se selecteaza limita cati urmaritori vrei pentru fiecare user din lista
        isOkOptionLimit = True
        while isOkOptionLimit:
            try:
                limitInput = int(input('Limita de postari pentru a da like, 0 - Exit \n'))  
                if limitInput == 0:
                    exit
                isOkOptionLimit = False    
            except ValueError:
                print('Optiunea selectata nu este valida!')

        return limitInput


    def checkAndReturnLimitCommentPosts(self):
        isOkOptionLimit = True
        while isOkOptionLimit:
            try:
                limitInput = int(input('Limita de postari pentru a comenta, 0 - Exit \n'))  
                if limitInput == 0:
                    exit
                isOkOptionLimit = False    
            except ValueError:
                print('Optiunea selectata nu este valida!')

        return limitInput

    
    def checkAndReturnSmartFollow(self):
        isOkOptionLimit = True
        while isOkOptionLimit:
            try:
                smart_follow = int(input('Follow doar la persoanele ce urmaresc mai multe persoane?, 1 - DA, 0 - NU \n'))  
                if smart_follow == 0:
                    exit
                isOkOptionLimit = False    
            except ValueError:
                print('Optiunea selectata nu este valida!')

        return smart_follow



    
    def checkAndReturnPath(self):
        isOkOptionPath = True
        while isOkOptionPath:
            pathInput = input("Calea catre fisierul .txt!, 0 - Exit \n")
            if pathInput == '0':
                exit

            if not pathInput.strip():
                isOkOptionPath = True
                print("Fisierul nu poate fi gol!")
            else:
                isOkOptionPath = False

            isFile = os.path.isfile(pathInput)
            
            if not isFile:
                isOkOptionPath = True
                print('Fisierul nu exista !')
            else:
                isOkOptionPath = False
        
        return pathInput




    def showMenuOptions(self):
        isMenuShow = True
        while isMenuShow:
            menuOptions = input('Meniu: \n' 
                                '1 - Comenteaza la urmaritorii unor useri \n' 
                                '2 - Apreciaza postarile urmaritorilor unor useri \n' 
                                '3 - Urmareste urmaritorii unor useri \n'
                                '4 - Apreciaza postarile unor useri \n'
                                '5 - Apreciaza postarile unor hashtag-uri\n'
                                '6 - Comenteaza postarile unor hashtag-uri\n'
                                '7 - Comenteaza la postarile unor useri\n'
                                '0 - Exit\n')     

            if int(menuOptions) == 1:
                #comenteaza la urmaritorii unor useri (se comenteaza doar la prima poza) 
                # prima data se selecteaza limita cati urmaritori vrei pentru fiecare user din lista
                limitInput = self.checkAndReturnLimitInput()
                pathInput  = self.checkAndReturnPath()
                smart_follow  = -1
                
                dictionary = {}
                with open(pathInput) as fp:
                    for line in fp.readlines():
                        line = line.strip()
                        user, comment = line.split(",")
                        dictionary[user] = comment

                return int(menuOptions), dictionary, int(limitInput), int(smart_follow)

            elif int(menuOptions) == 2:
                
                limitInput = self.checkAndReturnLimitInput()
                pathInput  = self.checkAndReturnPath()
                smart_follow = -1

                user_list = []
                with open(pathInput) as fp:
                    for line in fp.readlines():
                        line = line.strip()
                        user_list.append(line)

                return int(menuOptions), user_list, int(limitInput), int(smart_follow)
                
            elif int(menuOptions) == 3:
                limitInput = self.checkAndReturnLimitInput()
                pathInput = self.checkAndReturnPath()
                smart_follow = self.checkAndReturnSmartFollow()

                user_list = []
                with open(pathInput) as fp:
                    for line in fp.readlines():
                        line = line.strip()
                        user_list.append(line)

                return int(menuOptions), user_list, int(limitInput), int(smart_follow)
                
            elif int(menuOptions) == 4:
                limitInput = self.checkAndReturnLimitLikePosts()
                pathInput = self.checkAndReturnPath()
                smart_follow  = -1 
                user_list = []
                with open(pathInput) as fp:
                    for line in fp.readlines():
                        line = line.strip()
                        user_list.append(line)
                
                return int(menuOptions), user_list, int(limitInput), int(smart_follow)

            elif int(menuOptions) == 5:
                limitInput = self.checkAndReturnLimitLikePosts()
                pathInput = self.checkAndReturnPath()
                smart_follow = -1
                user_list = []
                with open(pathInput) as fp:
                    for line in fp.readlines():
                        line = line.strip()
                        user_list.append(line)

                return int(menuOptions), user_list, int(limitInput), int(smart_follow)

            elif int(menuOptions) == 6:
                limitInput = 0
                pathInput  = self.checkAndReturnPath()
                smart_follow = -1
                
                dictionary = {}
                with open(pathInput) as fp:
                    for line in fp.readlines():
                        line = line.strip()
                        hashtag, comment = line.split(",")
                        dictionary[hashtag] = comment

                return int(menuOptions), dictionary, int(limitInput), int(smart_follow)

            elif int(menuOptions) == 7:
                limitInput = 0
                pathInput  = self.checkAndReturnPath()
                smart_follow = -1
                
                dictionary = {}
                with open(pathInput) as fp:
                    for line in fp.readlines():
                        line = line.strip()
                        user, comment = line.split(",")
                        dictionary[user] = comment

                return int(menuOptions), dictionary, int(limitInput), int(smart_follow)

            elif int(menuOptions) == 0:
                isMenuShow = False  
                dictionary = {}
                limitInput = 0
                smart_follow = -1
                return int(menuOptions), dictionary, int(limitInput), int(smart_follow)
            else:
                print('Optiunea selectata nu exista!')