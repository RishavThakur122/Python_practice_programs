from datetime import date
from datetime import time
from datetime import datetime
# calling the today
# function of date class
today = date.today()

# Converting the date to the string
Str = date.isoformat(today)
print("in String ", Str)
print(type(Str))

# Creating Time object
Time = time(12,24,36,1212)

# Converting Time object to string
Str1 = Time.isoformat()
print("in String :", Str1)
print(type(Str1))

a = datetime(1999, 12, 12)
print(a)
 
# Initializing constructor
# with time parameters as well
a = datetime(1999, 12, 12, 12, 12, 12, 342380)
print(a)
