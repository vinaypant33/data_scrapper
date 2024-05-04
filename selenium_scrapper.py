from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By

from time import sleep
import winsound
from tqdm import tqdm

from tkinter import messagebox

frequency   = 2000
duration  = 2000


class selenium_driver():

    def __init__(self , current_roll_number  , sleep ) -> None:
        self.frequency  = 2000
        self.duration  = 2000
        self.current_roll_numebr  = current_roll_number
        self.registration_number  = "1171530224"
        self.sleep = sleep
        self.nodes = {'C': 1635,'D': 1835,'E': 2060,'S': 1945,'F': 2183,'G': 2450,'A': 2750,'B': 3087,' ': 37}

        self.driver  = webdriver.Firefox()
        # self.driver.maximize_window()
        self.driver.get("https://result.mdurtk.in/postexam/result.aspx")

    def check_rollnumber(self ):
        print("Checking the roll number with "  + str(self.current_roll_numebr))
        if self.driver.title == "Maharshi Dayanand University, Rohtak":
            self.driver.find_element(By.ID , "txtRegistrationNo").send_keys(str(self.registration_number))
            self.driver.find_element(By.ID , "txtRollNo").send_keys(str(self.current_roll_numebr))
            sleep(self.sleep)
            self.driver.find_element(By.ID , "cmdbtnProceed").click()
            sleep(self.sleep)
            try:
                mobile_number  = self.driver.find_element(By.ID , "txtMobileNo")
                mobile_number_confirmation  = self.driver.find_element(By.ID , "txtMobileNoCon")
                email_id_confirmation  = self.driver.find_element(By.ID , "txtEMail")
                confirm_click = self.driver.find_element(By.ID , "imgComfirm" )
                mobile_number.send_keys("9650849971")
                mobile_number_confirmation.send_keys("9650849971")
                email_id_confirmation.send_keys("vinaypant24@gmail.com")
                confirm_click.click()
            except:
                self.driver.close()
                self.driver.quit()
                with open("data_scrapper_log.txt" , 'a') as file : file.write("Mobile Number and Email ID not found for roll number :" + str(self.current_roll_numebr))
                return "Result Not Found"
            sleep(self.sleep)
            self.driver.find_element(By.ID , "imgComfirm").click()
            with open("working_rollnumber.txt" , 'a') as file : file.write("Successful Rollnumber : " + str(self.current_roll_numebr) + "\n")
            winsound.Beep(2000 , self.duration)
            messagebox.showinfo("Data Scrapper" , "Working Rollnumber Found : " + str(self.current_roll_numebr))
            return "Working Roll Number Found"

            # This code will be done in another class in the main loop of the tkinter library which will run using the thread pool and / which to be controlled by the slider
            # with open('confirmed_rollnumber.txt', 'a') as file: file.write(each)
        else:
            winsound.Beep(self.nodes['C'] , self.duration)
            print( "Title Not Found Aborting Borwser")
        self.driver.close()
        self.driver.quit()
        print("Quitting the browser")
        


if __name__ == '__main__':
    hehe  = selenium_driver(5434453 , 3 )
    hehe.check_rollnumber()