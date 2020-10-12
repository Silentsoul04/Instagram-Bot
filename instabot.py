''' Instagram Bot v 1.0.0.1'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os
import random
import getpass
from Menu import MenuOptions

class InstagramBot:
    def __init__(self , username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome('./chromedriver') # initializam o noua instanta de chromedriver
       
        self.login() # se apeleaza aici pentru a face direct login cand deschidem programul


    def random_number_generator(self, x, y):
        random_number = random.randrange((x * 100), (y * 100)) / 100
        return random_number

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login')
        sleep(self.random_number_generator(2, 4))
        self.driver.find_element_by_name('username').send_keys(self.username)
        passwordField = self.driver.find_element_by_name('password')
        passwordField.send_keys(self.password)
        passwordField.send_keys(Keys.RETURN)
        sleep(self.random_number_generator(2, 5))

    def nav_user(self, user):
        sleep(self.random_number_generator(2, 6))
        self.driver.get('https://instagram.com/' + user)

    def follow_user(self, user):
        self.nav_user(user)
        follow_button = self.driver.find_elements_by_xpath("//button[contains(text(), 'Follow')]")[0]
        follow_button.click()


    
    def like_user_post(self,user, limit = 3):
        try:
            self.nav_user(user)
            photo = self.driver.find_element_by_class_name('eLAPa')
            photo.click()
            sleep(self.random_number_generator(2, 7))
            for _ in range(limit):
                like_btn = self.driver.find_elements_by_class_name('wpO6b ')[2]
                sleep(self.random_number_generator(2, 7))
                like_btn.click()
        
                next_btn = self.driver.find_element_by_xpath("//a[contains(text(), 'Next')]")
                sleep(self.random_number_generator(1, 3))
                next_btn.click()
                sleep(self.random_number_generator(3, 6))
        except:
            pass


    def like_tag_post(self, tag, limit = 10):
        self.driver.get('https://instagram.com/explore/tags/' + tag)
        sleep(self.random_number_generator(2, 4))
        photo = self.driver.find_element_by_class_name('eLAPa')
        photo.click()
        sleep(self.random_number_generator(3 ,5))
        for _ in range(limit):
            like_btn = self.driver.find_elements_by_class_name('wpO6b ')[1]
            like_btn.click()
            sleep(self.random_number_generator(2, 4))
            next_btn = self.driver.find_element_by_xpath("//a[contains(text(), 'Next')]")
            next_btn.click()
            sleep(self.random_number_generator(3, 7))

    def users_followers(self, user, limit = 30):
        self.nav_user(user)
        sleep(self.random_number_generator(2, 4))
        followers_btn = self.driver.find_element_by_xpath(f"//a[contains(@href, '/{user}/followers/')]")
        followers_btn.click()
        sleep(self.random_number_generator(2, 4))
        fBody = self.driver.find_element_by_xpath("//div[@class='isgrP']")
        scroll = 0
        while scroll < 5:
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
            scroll += 1
            sleep(1)

        followers_list = []
        for i in range(limit):
            follower = self.driver.find_elements_by_class_name('FPmhX')[i]
            followers_list.append(follower.text)

        print(followers_list)
        return followers_list

    def follow_users(self,users, isSmartFollow):
        if isSmart_follow == 1:
            for user in users:   
                self.smart_follow(user)
        else:
            for user in users:
                self.follow_user(user)

    def like_users_posts(self, users):
        for user in users:
            self.like_user_post(user)

    def smart_follow_check(self, user):
        try:
            self.nav_user(user)
            followers = self.driver.find_element_by_xpath(f'//a[contains(@href, "{user}/followers")]/span')
            string = followers.text
            string = string.replace(',', '')
            followers_number = int(string)

            following = self.driver.find_element_by_xpath(f'//a[contains(@href, "{user}/following")]/span')
            string1 = following.text
            string1 = string1.replace(',', '')
            following_number = int(string1)
            if following_number > followers_number:
                return True
        
            return False
        except:
            pass

    # Follow user daca urmareste mai multi oameni de cat e urmarit
    def smart_follow(self, user):
        if self.smart_follow_check(user) == True:
            self.follow_user(user)

    #comenteaza la prima poza cu un hashtag specific
    def comment_post(self, tag, comment):
        self.driver.get(f'https://instagram.com/explore/tags/{tag}/')
        sleep(self.random_number_generator(2, 4))
        photo = self.driver.find_element_by_class_name('eLAPa')
        photo.click()
        sleep(2)
        comment_button = self.driver.find_elements_by_class_name('_8-yf5 ')[6]
        comment_button.click()
        sleep(2)
        comment_field = self.driver.find_element_by_class_name('Ypffh')
        comment_field.send_keys(comment)
        sleep(2)
        post = self.driver.find_element_by_xpath('//button[contains(text(), "Post")]')
        post.click()


    #comenteaza la prima poza a unui user    
    # e bagat in try except deoarece exista posibilitatea sa fie un profil privat
    def comment_user_post(self, user, comment):
        try:
            self.nav_user(user)
            sleep(self.random_number_generator(2, 4))
            photo = self.driver.find_element_by_class_name('eLAPa')
            photo.click()
            sleep(2)
            comment_button = bot.driver.find_element_by_class_name('_JgwE')
            comment_button.click()
            sleep(2)
            comment_field = self.driver.find_element_by_class_name('Ypffh')
            sleep(2)
            comment_field.send_keys(comment)
            sleep(2)
            post = self.driver.find_element_by_xpath('//button[contains(text(), "Post")]')
            post.click()
        except:
            pass


    def comment_users_post(self, users, comment):
        for user in users:
            self.comment_user_post(user, comment)


    # like primele 3 postari a unui nou follower de la un user specific
    def like_user_followers(self, user, limit=30):
        users = self.users_followers(user, limit=limit)
        self.like_users_posts(users)

    # coment la prima postare a unui nou follower a unui user specific
    # limita se foloseste la cati aduna prin scroll
    def comment_user_followers(self, user, comment, limit=30):
        users = self.users_followers(user, limit=limit)
        self.comment_users_post(users, comment)

    # follow un nou follower a unui user specific 
    # foloseste smartFollow
    def follow_user_followers(self, user, isSmartFollow, limit=30):
        users = self.users_followers(user, limit=limit)
        self.follow_users(users,isSmartFollow)


if __name__ == '__main__':
    menu = MenuOptions()
    menu.showTextAscii('Instagram Bot')
    username = input('Tasteaza user-ul de Instagram \n')
    password = getpass.getpass() 
    isApp = True
    while isApp:
        selectedOptions, returnDictionary, returnLimitInput, isSmart_follow = menu.showMenuOptions()
        if selectedOptions == 0:
            isApp = False
        elif selectedOptions == 1:
            try:
                bot = InstagramBot(username,password)
                for user_key, comment_value in returnDictionary.items():
                    bot.comment_user_followers(user_key, comment_value, returnLimitInput)
            except:
                bot.driver.close()
                print('A intervenit o eroare de autentificare sau userul nu a fost gasit! \nVa rugam reincercati!')

        elif selectedOptions == 2:
            # citeste urmaritorii cati ii dai tu si apoi da like la primele 3 postari ale lor
            try:
                bot = InstagramBot(username,password)
                for user_value in returnDictionary:
                    bot.like_user_followers(user_value,returnLimitInput)
            except:
                bot.driver.close()
                print('A intervenit o eroare de autentificare sau userul nu a fost gasit! \nVa rugam reincercati!')

        elif selectedOptions == 3:
            # citeste urmaritorii cati ii dai tu in limita si apoi da folllow la urmaritorii persoanelor din lista data de tine
            try:
                bot = InstagramBot(username, password)
                for user_value in returnDictionary:
                    bot.follow_user_followers(user_value,isSmart_follow,returnLimitInput)
            except:
                bot.driver.close()
                print('A intervenit o eroare de autentificare sau userul nu a fost gasit! \nVa rugam reincercati!')

        elif selectedOptions == 4:
            # se citeste din fisier userul si se stabileste limita la cate postari doresti sa dai like si da like
            try:
                bot = InstagramBot(username,password)
                for user_value in returnDictionary:
                    bot.like_user_post(user_value, returnLimitInput)
            except:
                bot.driver.close()
                print('A intervenit o eroare de autentificare sau userul nu a fost gasit! \nVa rugam reincercati!')
        elif selectedOptions == 5:
            #se citeste din fisier hashtag-urile si se stabileste limita la cate postari doresti sa dai like si da like 
            try:
                bot = InstagramBot(username, password)
                for hashtag_value in returnDictionary:
                    bot.like_tag_post(hashtag_value,returnLimitInput)
            except:
                bot.driver.close()
                print('A intervenit o eroare de autentificare sau userul nu a fost gasit! \nVa rugam reincercati!')
        elif selectedOptions == 6:
            # se da dintr-o lista de hashtaguri si se comenteaza la prima postare
            try:
                bot = InstagramBot(username,password)
                for hashtag_key, comment_value in returnDictionary.items():
                    bot.comment_post(hashtag_key, comment_value)
            except:
                bot.driver.close()
                print('A intervenit o eroare de autentificare sau userul nu a fost gasit! \nVa rugam reincercati!')
        
        elif selectedOptions == 7:
            try:
                bot = InstagramBot(username,password)
                for user_key, comment_value in returnDictionary.items():
                    bot.comment_user_post(user_key, comment_value)
            except:
                bot.driver.close()
                print('A intervenit o eroare de autentificare sau userul nu a fost gasit! \nVa rugam reincercati!')


