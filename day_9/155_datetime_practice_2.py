# Create an object in the today variable that always stores the current date when called.

import datetime
from datetime import date 

today=datetime.datetime.now()
print(today)

today=date.today()
print(today)