import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it will charge you 2 dollars a day")
elif type == "t2.mediam":
    print("it will charge you 4 dollars a day")
elif type == "t2.large":
    print("it will charge you 8 dollars a day") 
       
else:
    print("your input is not t2.micro, so we connot create")    