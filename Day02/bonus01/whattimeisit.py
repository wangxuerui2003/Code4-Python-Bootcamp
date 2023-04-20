from datetime import datetime
import pytz

local_timezone = pytz.timezone('Singapore')
local_time = datetime.now(local_timezone).strftime('%H:%M:%S.%f')

print(local_time)