from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random




class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r""
        )
        """ # after the 'r' put the directory of your geckodriver """
        # GeckoDriver link: https://github.com/mozilla/geckodriver/releases
        # Firefox link https://www.mozilla.org/pt-BR/firefox/new/

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(2)
        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)
        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)
        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.look_for_the_post()

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        """ This function will make the bot appear a humang typing """
        print("going to start typing message into message share text area")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1, 5) / 30)

    def look_for_the_post(self):
        
        driver = self.driver
        driver.get("link")#paste here the link of the post which you want to comment on 
        time.sleep(3)
        for i in range(
            1, 3
        ):  
            loop = True
            while loop == True:
                try:
                    # write here the comments which you want the bot to do 
                    comments = [
                    "comment",
                    "comment",
                    "comment",
                    "comment",
                    "comment",
                    "comment",
                    "comment",
                 ]  
                    driver.find_element_by_class_name("Ypffh").click()
                    comment_input_box = driver.find_element_by_class_name("Ypffh")
                    time.sleep(random.randint(2, 5))
                    self.type_like_a_person(
                    random.choice(comments), comment_input_box)
                    time.sleep(random.randint(3, 5))
                    driver.find_element_by_xpath(
                    "//button[contains(text(), 'Publicar')]" # depending on the language you are using for instagram, you'll need to change the 'Publicar' to publish in your language
                    ).click()
                    time.sleep(random.randint(3, 5))
                    loop = True
                except Exception as e:
                    print(e)
                    time.sleep(2)
            


# Write your login and password here
InstaBot = InstagramBot("username", "password")
InstaBot.login()
#if you want the bot to stop commenting, delete the terminal which it is running, and if you want to start again, just click run 