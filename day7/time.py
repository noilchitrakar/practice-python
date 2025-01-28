#should great the user good afternoon,good evening and goodnight
import time as t

timestamp=int(t.strftime("%H"))

if (timestamp>=6 and timestamp<12):
    print('good morning')
    print(f'The current time is',t.strftime("%H"))
elif(timestamp>=12 and timestamp<=12+5):
    print('good afternoon')
    print(f'The current time is',t.strftime("%H"))
elif(timestamp>12+5 and timestamp<=12+8):
    print('good afternoon')
    print(f'The current time is',t.strftime("%H"))
else:
    print("Good Night")
    print(f'The current time is',t.strftime("%H"))
a=input('do you want to know the Date?')
if a.lower()=='yes':
    print("the date is",t.strftime("%D"))
else:
    print("okay thanks for using the date and time information software")

