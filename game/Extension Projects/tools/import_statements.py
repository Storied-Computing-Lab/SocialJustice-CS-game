"Before using a library one needs to import that library into the file they are working on"

#For example before using the python time library, one needs to import like such:
import time

def func(x):
    while x!= 0:
        x =-1
        print ("a")

#If I wanted to time how long it takes to print x times I could use the time library like this:
def main ():
    start_time = time.time()
    func(100)
    print("total time taken to print 100 times: ", time.time() - start_time)