# In a variable called minutes, store only the minutes of the current time.

# For example, if it were to run at 20:43:17 at night, the variable minutes would store the value 43

from datetime import datetime

 
minutes_ = datetime.now().minute
print(minutes_)

import datetime
minutes=datetime.datetime.now()
print(minutes.strftime("%M"))