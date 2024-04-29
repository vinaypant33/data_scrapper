import tkinter as tk 
from tkinter import ttk
import customtkinter as ctk
import ttkbootstrap as btk
from tkinter import filedialog




def load_file():
    filename  =filedialog.askopenfilename()
    selected_file_text.delete( 0 , 100)
    selected_file_text.insert(0 , filename)
    return filedialog

def slider_value_func(value):
    borwser_value.configure(text = "Browser Count ( Threads ) : " + str(value))


def sleep_slider_value_func(value):
    sleep_value.configure(text = "Sleep Value: " + str(value))

def file_saving():
    save_file_dialog  = filedialog.asksaveasfilename()
    save_file_text.insert(0 , save_file_dialog)

# For now going with the file 
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

start_scrapping  = ctk.CTkButton(main_window , text="Start Scrapping" , width=255)
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