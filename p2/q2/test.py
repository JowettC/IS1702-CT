from urllib.request import urlretrieve
import os

def download(url, file):
  if os.path.isfile(file):
    print(file + " already downloaded. You can see it if you click on the folder icon at the left")
  else:
    print("Downloading file " + file + " ...", end="")
    urlretrieve(url,file)
    print("OK")

download('http://red.smu.edu.sg/resources/GraphLab.py','GraphLab.py')  # GraphLab
download('http://red.smu.edu.sg/resources/case1.csv','case1.csv')      # case1.csv
download('http://red.smu.edu.sg/resources/case1a.csv','case1a.csv')    # case1a.csv
download('http://red.smu.edu.sg/resources/case1b.csv','case1b.csv')    # case1b.csv (DAG)
download('http://red.smu.edu.sg/resources/case2.csv','case2.csv')      # case2.csv
download('http://red.smu.edu.sg/resources/case2a.csv','case2a.csv')    # case2a.csv (DAG)
download('http://red.smu.edu.sg/resources/case3.csv','case3.csv')      # case3.csv
download('http://red.smu.edu.sg/resources/case3a.csv','case3a.csv')    # case3a.csv (DAG)