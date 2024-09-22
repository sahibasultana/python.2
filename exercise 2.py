import time
# timestamp=time.strftime("%H:%M:%S") 
# print(timestamp)
# timestamp=time.strftime("%H") 
# print(timestamp)
# timestamp=time.strftime("%M") 
# print(timestamp)
# timestamp=time.strftime("%S") 
# print(timestamp)


# morningtime:04:00:00 t0 11:59:59
# afternoon time:12:00:00 to 17:00:00
# nighttime:21:00:00 t0 03:59:59
hours=int(time.strftime('%H'))
if(hours>=0 and hours<=11):
 print("hello good morning")
elif(hours>11 and hours<=17):
 print("hello good afternoon")
else:
 print("hello good night")

