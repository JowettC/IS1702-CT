from urllib.request import urlretrieve
import os

def download(url, file):
    if os.path.isfile(file):
        print(file + " already downloaded. You can see it if you click on the folder icon at the left")
    else:
        print("Downloading file " + file + " ...", end="")
        urlretrieve(url,file)
        print("OK")

download('http://red.smu.edu.sg/resources/case1.csv','./Lab4/case1.csv')  # case1.csv
download('http://red.smu.edu.sg/resources/case2.csv','./Lab4/case2.csv')  # case2.csv
download('http://red.smu.edu.sg/resources/case3.csv','./Lab4/case3.csv')  # case3.csv
download('http://red.smu.edu.sg/resources/case4.csv','./Lab4/case4.csv')  # case4.csv
download('http://red.smu.edu.sg/resources/case5.csv','./Lab4/case5.csv')  # case5.csv