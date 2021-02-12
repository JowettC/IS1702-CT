from urllib.request import urlretrieve
import os

def download(url, file):
    if not os.path.isfile(file):
        print("Download file... " + file + " ...")
        urlretrieve(url,file)
        print("File downloaded")

download('http://red.smu.edu.sg/resources/employees_10.csv','employees_10.csv')        # for lab 2a
download('http://red.smu.edu.sg/resources/employees_1mil.csv','employees_1mil.csv')    # for lab 2a
download('http://red.smu.edu.sg/resources/employees_birthyear_10.csv','employees_birthyear_10.csv')     # for lab 2b
download('http://red.smu.edu.sg/resources/employees_birthyear_1mil.csv','employees_birthyear_1mil.csv') # for lab 2b