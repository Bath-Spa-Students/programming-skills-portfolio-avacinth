# Exercise 3: Print date and Time 

from datetime import datetime

# datetime object containing current date and time
now = datetime.now()
 
print("now =", now)

# mm/dd/YY H:M:S
dt_string = now.strftime("""%m/%d/%Y
                 %H:%M:%S""")
print("date and time =", dt_string)