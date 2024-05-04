
from threading import thread
import threading




stop_event  = threading.Event()
threads = [] 


def calling_selenium_class(task_id , current_roll_number):

    pass



def thread_calling(thread_number):
    if len()
    pass



def button_click():
    ''' This will check if the list of the threads if more than 5 or 10 or the value of the thread count then dont make any new thread or else make new thread and then start the
    selenium class 
    '''

        
    for i in range(5):
        thread  = threading.Thread(target=thread_calling , args=(i ,))
        threads.append(thread)
        thread.start()
        for thread in threads():
            thread.join()

    print("All threads have finishied")

