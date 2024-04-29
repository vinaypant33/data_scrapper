from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from time import sleep
import winsound
from tqdm import tqdm

frequency   = 2000
duration  = 2000


class selenium_driver():

    def __init__(self , frequency , duration , loaded_rollnumbers , baseurl ) -> None:
        self.frequency  = frequency
        self.duration  = duration
        self.loaded_rollnumber  = loaded_rollnumbers
        self.registration_number  = ""
        self.nodes = {'C': 1635,'D': 1835,'E': 2060,'S': 1945,'F': 2183,'G': 2450,'A': 2750,'B': 3087,' ': 37}

        self.driver  = webdriver.Firefox()
        # self.driver.maximize_window()
        self.driver.get("https://www.google.com")

    def check_rollnumber(self):
        if self.driver.title == "Maharshi Dayanand University, Rohtak":
            self.driver.find_element(By.ID , "txtRegistrationNo").send_keys("1171530224")
        else:
            winsound.Beep(self.nodes['C'] , self.duration)
            print( "Title Not Found Aborting Borwser")
            self.driver.quit()
        


if __name__ == '__main__':
    hehe  = selenium_driver(2000 , 2000 , 3 , 3)
    hehe.check_rollnumber()