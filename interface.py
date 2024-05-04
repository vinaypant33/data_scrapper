import tkinter as tk 
from tkinter import ttk
import customtkinter as ctk
import ttkbootstrap as btk
from tkinter import filedialog 
import selenium_scrapper
import threading 
from time import sleep
import winsound
import concurrent.futures # For threadpool 
from tkinter import messagebox



## Setting up Constants  : 
current_working = True
current_sleep_value = 1
current_thread_value  = 1
loaded_rollnumber  = []
current_filename  = ""

stop_event  = threading.Event() # Will be used for the stop event of the threads 
lock  = threading.Lock() # Will be used for the locking of the threads
threads = []
current_count  = 0


def load_file():
    filename  =filedialog.askopenfilename()
    selected_file_text.delete( 0 , 100)
    selected_file_text.insert(0 , filename)
    return filename


def slider_value_func(value):
    borwser_value.configure(text = "Browser Count ( Threads ) : " + str(value))


def sleep_slider_value_func(value):
    sleep_value.configure(text = "Sleep Value: " + str(value))


def file_saving():
    save_file_dialog  = filedialog.asksaveasfilename()
    save_file_text.insert(0 , save_file_dialog)



###### THREAD FUNCTIONS ############

def file_loading():
    print("File Reading")
    current_filename = selected_file_text.get()
    readfile  = open(current_filename , 'r')
    line  = readfile.readline()
    while True:
        # Get next line from file
        line = readfile.readline()
        # if line is empty
        # end of file is reached
        if not line:
            break
        loaded_rollnumber.append(line)
    print("File Loading Done - Starting the thread")



def scrapper_selenium(roll_number , sleep):

    global current_count
    current_count+= 1
    print(current_count)
    scrapper = selenium_scrapper.selenium_driver(current_roll_number=roll_number , sleep=sleep)
    scrapper.check_rollnumber()
 


def second_thread_calling():
    global current_thread_value
    global sleep_value
    current_thread_value = int(browser_slider.get())
    sleep_value = int(sleep_slider.get())
    





def thread_calling():
    file_loading() # File Loading for the roll number 
    global current_thread_value
    global sleep_value

    sleep_value = int(sleep_slider.get())

    print("Loaded Roll Number : " + str(len(loaded_rollnumber)))
    current_thread_value = int(browser_slider.get())
    print("Threads : " + str(current_thread_value))
    

    # for i in range(current_thread_value):
    #         current_rollnumber  = loaded_rollnumber.pop(0)
    #         # print("current rollnumber : " + str(current_rollnumber))
    #         # print("Current rollnumber count : " + str(len(loaded_rollnumber)))
    #         thread  = threading.Thread(target=scrapper_selenium , args=(current_rollnumber ,  sleep_value))
    #         thread.start()

    #         threads.append(thread)

    #         while True:
    #             alive_threads  = sum(1 for thread in threads if thread.is_alive())
    #             if alive_threads == 0:
    #                 print("Thread Count is Completed")
    #                 # break
    #                 # Setting up the thread 
    #                 second_thread_calling() # Calling the thread again and making a beep for the 
    #             else:
    #                 pass

    # with concurrent.futures.ThreadPoolExecutor(max_workers=current_thread_value) as executor:
    #     current_rollnumber  = loaded_rollnumber.pop(0)
    #     futures = [executor.submit(scrapper_selenium, current_rollnumber , sleep_value) for i in range(current_thread_value)]
    #     for future in concurrent.futures.as_completed(futures):
    #         print("All threads are completed")

    executor = concurrent.futures.ThreadPoolExecutor(max_workers=current_thread_value)


    futures = [executor.submit(scrapper_selenium, loaded_rollnumber.pop(0), sleep_value) for _ in range(5)]
        # Wait for all futures to complete
    for future in concurrent.futures.as_completed(futures):
        print("All threads are completed")

    # Close the executor manually
    executor.shutdown()

        

####### MAIN WINDOW #################


main_window  = ctk.CTk()
ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# --------

main_window.title("Web Scrapper")

# Maing the application in the center screen  : 
height  = 230
width  = 550


x_location  = (main_window.winfo_width() //2 ) + (width)
y_location  = (main_window.winfo_height() // 2) + (height)

main_window.geometry(f"{width}x{height}+{x_location}+{y_location}")
main_window.resizable(0 , 0)

# Defining the main controls :
select_file_button  = ctk.CTkButton(main_window , text="Select Password File" , command=load_file)
selected_file_text = ctk.CTkEntry(main_window , placeholder_text="Selected Password File : " , width=380)

borwser_value  = ctk.CTkLabel(main_window , text="Browser Count ( Threads ) : 5.0")
browser_slider =ctk.CTkSlider(main_window , from_= 0 , to=10 , number_of_steps=10,width =250 ,  command=slider_value_func)

sleep_value  = ctk.CTkLabel(main_window , text="Sleep Value: 5.0")
sleep_slider =ctk.CTkSlider(main_window , from_= 1 , to=10 , number_of_steps=9, width =250,  command=sleep_slider_value_func)

# Saving the file : in text file after 200 iterations  : 
save_file_button = ctk.CTkButton(main_window , text="Save File" , command=file_saving)
save_file_text  = ctk.CTkEntry(main_window , placeholder_text="Enter File to Save Password" , width=380)


# Make start and stop buttons : 

start_scrapping  = ctk.CTkButton(main_window , text="Start Scrapping" , width=255 , command=thread_calling)
stop_scrapping  = ctk.CTkButton(main_window , text="Stop Scrapping" , width  = 255)


progress_bar  =ctk.CTkProgressBar(main_window , orientation='horizontal' , width=530 , height=10)
progress_bar.set(0.0)

status_bar  = ctk.CTkLabel(main_window , text="Status : ")



# Placing the buttons : 
select_file_button.place(x = 10 , y = 10)
selected_file_text.place(x = 155 , y= 10)
borwser_value.place(x  = 15 , y = 45)
browser_slider.place(x = 10 , y = 70)

sleep_value.place(x = 290 , y = 45)
sleep_slider.place(x = 280, y = 70)

save_file_button.place(x = 10 , y = 100)
save_file_text.place(x = 155 , y = 100)

# Place the buttons : Start Scrapping and Stop Scrapping 
start_scrapping.place(x = 10 , y = 145)
stop_scrapping.place(x= 280 , y  =145)


progress_bar.place(x = 10 , y = 190)
status_bar.place(x = 10 , y = 200)

main_window.mainloop()