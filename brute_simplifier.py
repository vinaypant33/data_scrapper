from tkinter import filedialog
from tqdm import tqdm



file_name  = filedialog.askopenfilename()

readfile  = open(file_name , 'r')
line  = readfile.readline()


while True:

    for i in tqdm(range(int(9999999))):
    
        # Get next line from file
        line  = readfile.readline()
        # if line is empty
        # end of file is reached
        if not line:
            break
        if line.strip().startswith('2') or line.strip().startswith('5'):
            with open('final_one.txt', 'a') as file: file.write( line )
    pass
    

print("Done")